import telebot
from telebot import types
from messages import Messages
import random

# Создаем экземпляр бота
bot = telebot.TeleBot('5839845850:AAHtIvxrAMgxAmI8JR4lSJEUXbVUYiLchj0')

mes = Messages()

channel_link = ["https://t.me/+pgSMhr10-R0yOTIy"]

subscriptions = {}


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем объект клавиатуры
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

    # Создаем кнопку для запроса контакта
    contact_button = types.KeyboardButton(text="Отправить контакт", request_contact=True)

    # Добавляем кнопку на клавиатуру
    keyboard.add(contact_button)

    # Отправляем приветственное сообщение с клавиатурой
    bot.send_message(message.chat.id, "Привет! Пожалуйста, отправь мне свой контакт.", reply_markup=keyboard)


# Обработчик полученного контакта
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    contact = message.contact
    phone_number = contact.phone_number
    first_name = contact.first_name
    last_name = contact.last_name if contact.last_name else ""

    # Обрабатываем полученный контакт
    # Можно сохранить его в базу данных или выполнить другие действия

    # Отправляем подтверждение сбора контакта
    bot.send_message(message.chat.id, mes.message1(first_name))

    # Create a new keyboard with additional buttons
    new_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подписаться")
    button2 = types.KeyboardButton(text="Я подписался 👌")
    new_keyboard.add(button1, button2)

    # Send a message with the new keyboard
    bot.send_message(message.chat.id, mes.message2(), reply_markup=new_keyboard)


# Handler for button clicks
@bot.message_handler(func=lambda message: True)
def handle_button_click(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Подписаться":
        # Store the channel link in the subscriptions dictionary
        subscriptions[chat_id] = channel_link

        # Send the channel link to the user
        bot.send_message(chat_id, mes.message3(channel_link))

    elif text == "Я подписался 👌":
        # Check if the user is subscribed to the channel
        if chat_id in subscriptions:
            send_subscribed_message(chat_id)
        else:
            send_unsubscribed_message(chat_id)

    elif text == '🎁 Забрать "Анализ регионов MENA"':
        send_message_mena_analysis(chat_id)

    elif text == "Про OpenMENA":
        bot.send_message(chat_id, "пашол нахой")

    elif text == "Мероприятия":
        bot.send_message(chat_id, "пашол нахой")

    elif text == "Стать участником":
        bot.send_message(chat_id, "пашол нахой")

    elif text == "Стать партнером":
        bot.send_message(chat_id, "пашол нахой")

    elif text == "OpenCalifornia":
        bot.send_message(chat_id, "пашол нахой")

    elif text == "Подать заявку":
        bot.send_message(chat_id, "пашол нахой")

    elif text == "На главную":
        send_subscribed_message(chat_id)

# Send the analysis info
def send_message_mena_analysis(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Про OpenMENA")
    button2 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2)

    with open('doc.pdf', 'rb') as pdf:
        bot.send_document(chat_id, pdf, caption=mes.message5(), reply_markup=keyboard)


# Send the subscribed message
def send_subscribed_message(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='🎁 Забрать "Анализ регионов MENA"')
    button2 = types.KeyboardButton(text='Про OpenMENA')
    button3 = types.KeyboardButton(text='Мероприятия')
    button4 = types.KeyboardButton(text='Стать участником')
    button5 = types.KeyboardButton(text='Стать партнером')
    button6 = types.KeyboardButton(text='OpenCalifornia')
    button7 = types.KeyboardButton(text='Связаться с менеджером')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)

    bot.send_message(chat_id, mes.message6(), reply_markup=keyboard)


# Send the unsubscribed message
def send_unsubscribed_message(chat_id):
    message_text = "Your custom message for unsubscribed users."

    bot.send_message(chat_id, mes.message4())



# Запускаем бота
bot.polling()
