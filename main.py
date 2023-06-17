import telebot
import re
from telebot import types
from messages import Messages
import random

# Создаем экземпляр бота
bot = telebot.TeleBot('5839845850:AAHtIvxrAMgxAmI8JR4lSJEUXbVUYiLchj0')

mes = Messages()

channel_link = "https://t.me/+pgSMhr10-R0yOTIy"

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
        bot.send_message(chat_id, mes.message3(channel_link))

    elif text == "Я подписался 👌":
        channel_id, user_id = get_channel_user_ids(channel_link)

        print("Channel ID:", channel_id)
        print("User ID:", user_id)

        if is_user_subscribed(channel_id, user_id):
            send_subscribed_message(chat_id)
        else:
            send_unsubscribed_message(chat_id)

    elif text == '🎁 Забрать "Анализ регионов MENA"':
        send_message_1_ticket(chat_id)

    elif text == "Про OpenMENA":
        send_message_2_ticket(chat_id)

    elif text == "Мероприятия":
        send_message_3_ticket(chat_id)

    elif text == "Расписание и запись" or text == "Записаться":
        send_message_3a0_ticket(chat_id)

    elif text == "MEET up":
        send_message_3a_ticket(chat_id)

    elif text == "Academy":
        send_message_3b_ticket(chat_id)

    elif text == "Business Trip":
        send_message_3c_ticket(chat_id)

    elif text == "Стратсессии":
        send_message_3d_ticket(chat_id)

    elif text == "AMA сессии":
        send_message_3e_ticket(chat_id)

    elif text == "Стать участником":
        send_message_4_ticket(chat_id)

    elif text == "Стать партнером":
        send_message_5_ticket(chat_id)

    elif text == "OpenCalifornia":
        send_message_6_ticket(chat_id)

    elif text == "Связаться с менеджером":
        send_contact_message(chat_id)

    elif text == "Подать заявку":
        #TODO
        pass

    elif text == "На главную":
        send_subscribed_message(chat_id)


# Send the analysis info
def send_message_1_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Про OpenMENA")
    button2 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2)

    with open('doc.pdf', 'rb') as pdf:
        bot.send_document(chat_id, pdf, caption=mes.message5(), reply_markup=keyboard)


# Send the analysis info
def send_message_2_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Мероприятия")
    button2 = types.KeyboardButton(text="Стать участником")
    button3 = types.KeyboardButton(text="Стать партнёром")
    button4 = types.KeyboardButton(text="OpenCalifornia")
    button5 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4, button5)

    bot.send_message(chat_id, mes.message7(), reply_markup=keyboard)


# Send the analysis info
def send_message_3_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Расписание и запись")
    button2 = types.KeyboardButton(text="MEET up")
    button3 = types.KeyboardButton(text="Academy")
    button4 = types.KeyboardButton(text="Business Trip")
    button5 = types.KeyboardButton(text="Стратсессии")
    button6 = types.KeyboardButton(text="AMA сессии")
    button7 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)

    bot.send_message(chat_id, mes.message8(), reply_markup=keyboard)


# Send the analysis info
def send_message_3a0_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="На главную")
    keyboard.add(button1)
    message_form = "https://clck.ru/34Zn35"
    bot.send_message(chat_id, message_form, reply_markup=keyboard)


# Send the analysis info
def send_message_3a_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Записаться")
    button2 = types.KeyboardButton(text="Academy")
    button3 = types.KeyboardButton(text="Business Trip")
    button4 = types.KeyboardButton(text="Стратсессии")
    button5 = types.KeyboardButton(text="AMA сессии")
    button6 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4, button5, button6)

    bot.send_message(chat_id, mes.message12(), reply_markup=keyboard)


# Send the analysis info
def send_message_3b_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Записаться")
    button2 = types.KeyboardButton(text="MEET up")
    button4 = types.KeyboardButton(text="Business Trip")
    button5 = types.KeyboardButton(text="Стратсессии")
    button6 = types.KeyboardButton(text="AMA сессии")
    button7 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button4, button5, button6, button7)

    bot.send_message(chat_id, mes.message13(), reply_markup=keyboard)


# Send the analysis info
def send_message_3c_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Записаться")
    button2 = types.KeyboardButton(text="MEET up")
    button4 = types.KeyboardButton(text="Academy")
    button5 = types.KeyboardButton(text="Стратсессии")
    button6 = types.KeyboardButton(text="AMA сессии")
    button7 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button4, button5, button6, button7)

    bot.send_message(chat_id, mes.message14(), reply_markup=keyboard)


# Send the analysis info
def send_message_3d_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Записаться")
    button2 = types.KeyboardButton(text="MEET up")
    button4 = types.KeyboardButton(text="Business Trip")
    button5 = types.KeyboardButton(text="Academy")
    button6 = types.KeyboardButton(text="AMA сессии")
    button7 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button4, button5, button6, button7)

    bot.send_message(chat_id, mes.message15(), reply_markup=keyboard)


# Send the analysis info
def send_message_3e_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Записаться")
    button2 = types.KeyboardButton(text="MEET up")
    button4 = types.KeyboardButton(text="Business Trip")
    button5 = types.KeyboardButton(text="Academy")
    button6 = types.KeyboardButton(text="Стратсессии")
    button7 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button4, button5, button6, button7)

    bot.send_message(chat_id, mes.message16(), reply_markup=keyboard)


# Send the analysis info
def send_message_4_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подать заявку")
    button2 = types.KeyboardButton(text="Стать участником")
    button3 = types.KeyboardButton(text="Стать партнером")
    button4 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(chat_id, mes.message9(), reply_markup=keyboard)


# Send the analysis info
def send_message_5_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подать заявку")
    button2 = types.KeyboardButton(text="Стать участником")
    button3 = types.KeyboardButton(text="OpenCalifornia")
    button4 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(chat_id, mes.message10(), reply_markup=keyboard)


# Send the analysis info
def send_message_6_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Стать участником")
    button2 = types.KeyboardButton(text="Kанал OpenCalifornia")
    button3 = types.KeyboardButton(text="OpenCalifornia")
    button4 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(chat_id, mes.message11(), reply_markup=keyboard)


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


# Send the unsubscribed message
def send_contact_message(chat_id):
    first_name = 'John'
    last_name = 'Doe'
    phone_number = '+1234567890'

    # Send the contact
    bot.send_contact(chat_id, phone_number, first_name, last_name)


def is_user_subscribed(channel_id, user_id):
    try:
        # Use the get_chat_member method to check if the user is a member of the channel
        member_info = bot.get_chat_member(channel_id, user_id)

        # If the member status is 'member' or 'creator', the user is subscribed
        if member_info.status in ['member', 'creator']:
            return True
        else:
            return False
    except telebot.apihelper.ApiException:
        # An ApiException will occur if the bot is not a member of the channel
        return False


def get_channel_user_ids(channel_link):
    print(channel_link)

    # Extract the channel username or ID from the link
    match = re.search(r'(?:https?://)?(?:www\.)?t\.me/(joinchat/)?(?:invite/)?([a-zA-Z0-9_-]+)', channel_link)
    if match:
        channel_identifier = match.group(2)

        # Get the chat ID
        chat_id = None
        try:
            chat_id = int(channel_identifier)
        except ValueError:
            pass

        # Get the user ID
        user_id = None
        if not chat_id:
            try:
                user_id = int(channel_identifier)
            except ValueError:
                pass

        return chat_id, user_id

    return None, None


# Запускаем бота
bot.polling()
