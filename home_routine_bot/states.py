from aiogram.fsm.state import State, StatesGroup


class AddTask(StatesGroup):
    """FSM states for adding a task."""

    category = State()
    title = State()
    date = State()
