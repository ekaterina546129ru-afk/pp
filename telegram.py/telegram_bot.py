import telebot
import telebot.types
import sklad


bot = telebot.TeleBot("8799490361:AAFSrzHOAB3-oz5rQnyUTVjZpBkwJ9v7_CA")


@bot.message_handler(commands=["start"])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, sklad.COMMAND_START_OUTPUT_TEXT)


@bot.message_handler(commands=["schedule"])
def schedule(message: telebot.types.Message):
    reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_monday = telebot.types.KeyboardButton(sklad.BUTTON_MONDAY_TEXT)
    button_tuesday = telebot.types.KeyboardButton(sklad.BUTTON_TUESDAY_TEXT)
    button_wednesday = telebot.types.KeyboardButton(sklad.BUTTON_WEDNESDAY_TEXT)
    button_thursday = telebot.types.KeyboardButton(sklad.BUTTON_THURSDAY_TEXT)
    button_friday = telebot.types.KeyboardButton(sklad.BUTTON_FRIDAY_TEXT)
    button_saturday = telebot.types.KeyboardButton(sklad.BUTTON_SATURDAY_TEXT)

    reply_keyboard.add(button_monday)
    reply_keyboard.add(button_tuesday)
    reply_keyboard.add(button_wednesday)
    reply_keyboard.add(button_thursday)
    reply_keyboard.add(button_friday)
    reply_keyboard.add(button_saturday)

    bot.send_message(message.chat.id, sklad.COMMAND_SCHEDULE_OUTPUT_TEXT, reply_markup=reply_keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message: telebot.types.Message):
    input_text = message.text.lower()
    output_text = ""

    if input_text == sklad.BUTTON_MONDAY_TEXT.lower():
        output_text = sklad.SCHEDULE_MONDAY_OUTPUT_TEXT
        bot.send_message(message.chat.id, output_text)
    elif input_text == sklad.BUTTON_TUESDAY_TEXT.lower():
        output_text = sklad.SCHEDULE_TUESDAY_OUTPUT_TEXT
        bot.send_message(message.chat.id, output_text)
    elif input_text == sklad.BUTTON_WEDNESDAY_TEXT.lower():
        output_text = sklad.SCHEDULE_WEDNESDAY_OUTPUT_TEXT
        bot.send_message(message.chat.id, output_text)      
    elif input_text == sklad.BUTTON_THURSDAY_TEXT.lower():
        output_text = sklad.SCHEDULE_THURSDAY_OUTPUT_TEXT
        bot.send_message(message.chat.id, output_text)
    elif input_text == sklad.BUTTON_FRIDAY_TEXT.lower():
        output_text = sklad.SCHEDULE_FRIDAY_OUTPUT_TEXT
        bot.send_message(message.chat.id, output_text)
    elif input_text == sklad.BUTTON_SATURDAY_TEXT.lower():
        output_text = sklad.SCHEDULE_SATURDAY_OUTPUT_TEXT
        bot.send_message(message.chat.id, output_text)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите день недели из предложенных кнопок.")

print("Бот запущен...")
bot.infinity_polling()
