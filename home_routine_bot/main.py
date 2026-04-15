import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import BOT_TOKEN
from database import add_task, delete_task, get_tasks, init_db, mark_task_done
from keyboards import CATEGORIES, get_categories_keyboard, get_main_menu
from states import AddTask

# user_id -> action ('done' | 'delete')
pending_actions: dict[int, str] = {}


def format_tasks(tasks: list[tuple]) -> str:
    """Format tasks into numbered list."""
    if not tasks:
        return "\u041f\u043e\u043a\u0430 \u0437\u0430\u0434\u0430\u0447 \u043d\u0435\u0442. \u0414\u043e\u0431\u0430\u0432\u044c \u043f\u0435\u0440\u0432\u0443\u044e \u0437\u0430\u0434\u0430\u0447\u0443 \U0001F3E0"

    lines = []
    for index, task in enumerate(tasks, start=1):
        task_id, category, title, date_value, is_done = task
        done_mark = " \u2705" if is_done else ""
        lines.append(f"{index}. [ID {task_id}] [{category}] {title} \u2014 {date_value}{done_mark}")
    return "\n".join(lines)


async def show_menu(message: Message) -> None:
    await message.answer("\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e:", reply_markup=get_main_menu())


async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    pending_actions.pop(message.from_user.id, None)
    await message.answer(
        "\u041f\u0440\u0438\u0432\u0435\u0442! \u042f \u0431\u043e\u0442 \u0434\u043b\u044f \u0434\u043e\u043c\u0430\u0448\u043d\u0435\u0439 \u0440\u0443\u0442\u0438\u043d\u044b \U0001F3E0\n"
        "\u041f\u043e\u043c\u043e\u0433\u0443 \u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u043e\u043c\u0430\u0448\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438: \u0443\u0431\u043e\u0440\u043a\u0430, \u043f\u043e\u043a\u0443\u043f\u043a\u0438, \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u044f \u0438 \u0434\u0440\u0443\u0433\u043e\u0435."
    )
    await show_menu(message)


async def cmd_menu(message: Message, state: FSMContext) -> None:
    await state.clear()
    pending_actions.pop(message.from_user.id, None)
    await show_menu(message)


async def cmd_cancel(message: Message, state: FSMContext) -> None:
    pending_actions.pop(message.from_user.id, None)
    await state.clear()
    await message.answer("\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435 \u043e\u0442\u043c\u0435\u043d\u0435\u043d\u043e.", reply_markup=get_main_menu())


async def add_task_start(message: Message, state: FSMContext) -> None:
    pending_actions.pop(message.from_user.id, None)
    await state.set_state(AddTask.category)
    await message.answer(
        "\u0412\u044b\u0431\u0435\u0440\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0437\u0430\u0434\u0430\u0447\u0438:",
        reply_markup=get_categories_keyboard(),
    )


async def add_task_category(message: Message, state: FSMContext) -> None:
    category = message.text.strip()
    if category not in CATEGORIES:
        await message.answer("\u0412\u044b\u0431\u0435\u0440\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u043a\u043d\u043e\u043f\u043a\u043e\u0439 \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430.")
        return

    await state.update_data(category=category)
    await state.set_state(AddTask.title)
    await message.answer(
        "\u0412\u0432\u0435\u0434\u0438 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438. "
        "\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \u041f\u043e\u043b\u0438\u0442\u044c \u0444\u0438\u043a\u0443\u0441"
    )


async def add_task_title(message: Message, state: FSMContext) -> None:
    title = message.text.strip()
    if not title:
        await message.answer("\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u044b\u043c.")
        return

    await state.update_data(title=title)
    await state.set_state(AddTask.date)
    await message.answer(
        "\u0412\u0432\u0435\u0434\u0438 \u0434\u0430\u0442\u0443 \u0438\u043b\u0438 \u0447\u0430\u0441\u0442\u043e\u0442\u0443. "
        "\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: \u0437\u0430\u0432\u0442\u0440\u0430 / \u043a\u0430\u0436\u0434\u044b\u0435 3 \u0434\u043d\u044f"
    )


async def add_task_date(message: Message, state: FSMContext) -> None:
    date_value = message.text.strip()
    if not date_value:
        await message.answer("\u0414\u0430\u0442\u0430 \u0438\u043b\u0438 \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u043d\u0435 \u0434\u043e\u043b\u0436\u043d\u0430 \u0431\u044b\u0442\u044c \u043f\u0443\u0441\u0442\u043e\u0439.")
        return

    data = await state.get_data()
    add_task(
        user_id=message.from_user.id,
        category=data["category"],
        title=data["title"],
        date=date_value,
    )
    await state.clear()
    await message.answer("\u0417\u0430\u0434\u0430\u0447\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0430 \u2705", reply_markup=get_main_menu())


async def show_tasks(message: Message) -> None:
    tasks = get_tasks(message.from_user.id)
    await message.answer(format_tasks(tasks), reply_markup=get_main_menu())


async def mark_done_request(message: Message) -> None:
    tasks = get_tasks(message.from_user.id, only_not_done=True)
    if not tasks:
        await message.answer("\u041d\u0435\u0442 \u043d\u0435\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447.", reply_markup=get_main_menu())
        return

    pending_actions[message.from_user.id] = "done"
    await message.answer(
        format_tasks(tasks)
        + "\n\n\u0412\u0432\u0435\u0434\u0438 ID \u0437\u0430\u0434\u0430\u0447\u0438, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043d\u0443\u0436\u043d\u043e \u043e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439:",
        reply_markup=get_main_menu(),
    )


async def delete_task_request(message: Message) -> None:
    tasks = get_tasks(message.from_user.id)
    if not tasks:
        await message.answer("\u0423\u0434\u0430\u043b\u044f\u0442\u044c \u043f\u043e\u043a\u0430 \u043d\u0435\u0447\u0435\u0433\u043e.", reply_markup=get_main_menu())
        return

    pending_actions[message.from_user.id] = "delete"
    await message.answer(
        format_tasks(tasks)
        + "\n\n\u0412\u0432\u0435\u0434\u0438 ID \u0437\u0430\u0434\u0430\u0447\u0438, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043d\u0443\u0436\u043d\u043e \u0443\u0434\u0430\u043b\u0438\u0442\u044c:",
        reply_markup=get_main_menu(),
    )


async def process_task_id(message: Message) -> None:
    user_id = message.from_user.id
    action = pending_actions.get(user_id)
    if action is None:
        return

    text = message.text.strip()
    if not text.isdigit():
        await message.answer("\u041d\u0443\u0436\u043d\u043e \u0432\u0432\u0435\u0441\u0442\u0438 \u0447\u0438\u0441\u043b\u043e (ID \u0437\u0430\u0434\u0430\u0447\u0438).")
        return

    task_id = int(text)
    if action == "done":
        if mark_task_done(user_id, task_id):
            await message.answer("\u0417\u0430\u0434\u0430\u0447\u0430 \u043e\u0442\u043c\u0435\u0447\u0435\u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u2705", reply_markup=get_main_menu())
        else:
            await message.answer("\u0417\u0430\u0434\u0430\u0447\u0430 \u0441 \u0442\u0430\u043a\u0438\u043c ID \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430.")
    elif action == "delete":
        if delete_task(user_id, task_id):
            await message.answer("\u0417\u0430\u0434\u0430\u0447\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u0430 \U0001F5D1", reply_markup=get_main_menu())
        else:
            await message.answer("\u0417\u0430\u0434\u0430\u0447\u0430 \u0441 \u0442\u0430\u043a\u0438\u043c ID \u043d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d\u0430.")

    pending_actions.pop(user_id, None)


async def main() -> None:
    init_db()

    if BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        raise ValueError("\u0423\u043a\u0430\u0436\u0438\u0442\u0435 BOT_TOKEN \u0432 config.py")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_menu, Command("menu"))
    dp.message.register(cmd_cancel, Command("cancel"))

    dp.message.register(add_task_start, F.text == "\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443")
    dp.message.register(add_task_category, AddTask.category)
    dp.message.register(add_task_title, AddTask.title)
    dp.message.register(add_task_date, AddTask.date)

    dp.message.register(show_tasks, F.text == "\U0001F4CB \u041c\u043e\u0438 \u0437\u0430\u0434\u0430\u0447\u0438")
    dp.message.register(mark_done_request, F.text == "\u2705 \u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439")
    dp.message.register(delete_task_request, F.text == "\U0001F5D1 \u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443")

    dp.message.register(process_task_id)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
