import telebot
from telebot import types
from messages import Messages
import random
import requests

# Создаем экземпляр бота
bot = telebot.TeleBot('5839845850:AAHtIvxrAMgxAmI8JR4lSJEUXbVUYiLchj0')
url_ca = 'https://docs.google.com/forms/d/e/1FAIpQLSf2TDJR1j6BTLtB0sSsi286q0qR2h0t4Aq8Fx05Z_o8EjkNeQ/formResponse'
url_mena = 'https://docs.google.com/forms/d/e/1FAIpQLSdtXAzG6D39SPEFBtk17dFo_cgrniNCdP05tf67nV1-BNip-Q/formResponse'
mes = Messages()

channel_link = "https://t.me/testbot123da"
channel_id = [-1001930406351]
channel_open_california_link = "link to channel OpenCA"
channel_open_california_chat_link = 'link to chat OpenCA'
channel_open_mena_link = 'link to channel OpenMENA'
channel_open_mena_chat_link = 'link to chat OpenMENA'
subscriptions = {}

user_state_ca, user_state_mena, user_data_ca, user_data_mena, user_data_ca_for_post, user_data_mena_for_post = {}, {}, {}, {}, {}, {},

fields_for_ca = ['Имя Фамилия', 'Телефон для связи', 'Ваш Telegram', 'Email', 'В какой стране Вы живете?',
                 'Опишите деятельность Вашей компании?', 'Регион присутствия (в том числе планируемый) Вашей компании?',
                 'Как называется Ваша компания?', 'Ссылка на сайт компании', 'Годовой оборот Вашей компании?',
                 'Количество человек в Вашей команде?',
                 'Дополнительные направления бизнеса, которые Вы развиваете?',
                 'Вы хотите стать спикером на мероприятиях OpenCA?', 'На какие темы Вы хотите выступать?',
                 'Хотели бы Вы стать партнером OpenCA?',
                 'Цель участия в OpenCA', 'Какой из форматов встреч нравится и актуален для вас?']

fields_for_mena = ['Имя Фамилия', 'Телефон для связи', 'Ваш Telegram', 'Email', 'В какой стране Вы живете?',
                   'Опишите деятельность Вашей компании?',
                   'Регион присутствия (в том числе планируемый) Вашей компании?',
                   'Как называется Ваша компания?', 'Ссылка на сайт компании', 'Годовой оборот Вашей компании?',
                   'Количество человек в Вашей команде?',
                   'Дополнительные направления бизнеса, которые Вы развиваете?',
                   'Вы хотите стать спикером на мероприятиях OpenMENA?', 'На какие темы Вы хотите выступать?',
                   'Хотели бы Вы стать партнером OpenMENA?',
                   'Цель участия в OpenMENA', 'Какой из форматов встреч нравится и актуален для вас?']

form_entry = [
    'entry.91462916',
    'entry.630533396',
    'entry.2039931063',
    'entry.1318559028',
    'entry.1254544746',
    'entry.191036165',
    'entry.854259575',
    'entry.1448253998',
    'entry.729755307',
    'entry.601340499',
    'entry.292760203',
    'entry.1874047276',
    'entry.1566950839',
    'entry.104522551',
    'entry.281659691',
    'entry.2132372300',
    'entry.1885107982',
]

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
        try:
            channel_id = -1001954800199
            member = bot.get_chat_member(channel_id, chat_id)
            if member.status in ['creator', 'administrator', 'member', 'restricted']:
                send_subscribed_message(chat_id)
            else:
                send_unsubscribed_message(chat_id)
        except Exception as e:
            bot.send_message(chat_id, f'An error occurred: {e}')

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

    elif text == "На главную":
        send_subscribed_message(chat_id)


    #vlad code

    elif text == "Подать заявку":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="Заполнить анкету")
        button1 = types.KeyboardButton(text="На главную")
        keyboard.add(button, button1)
        bot.send_message(chat_id, mes.message7(), reply_markup=keyboard)

    elif text == "Стать участником OpenCA":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="Заполнить анкету OpenCA")
        button1 = types.KeyboardButton(text="На главную")
        keyboard.add(button, button1)
        bot.send_message(chat_id, mes.message7(), reply_markup=keyboard)

    elif text == "Заполнить анкету OpenCA":
        user_state_ca[chat_id] = 0
        user_data_ca[chat_id] = {}
        ask_question_ca(message)

    elif text == "Заполнить анкету":
        user_state_mena[chat_id] = 0
        user_data_mena[chat_id] = {}
        ask_question_mena(message)

    elif chat_id in user_state_ca:
        if text == "Пропустить":
            user_data_ca[chat_id][fields_for_ca[user_state_ca[chat_id]]] = ""
            user_data_ca_for_post[form_entry[user_state_ca[chat_id]]] = ""
        else:
            user_data_ca[chat_id][fields_for_ca[user_state_ca[chat_id]]] = text
            user_data_ca_for_post[form_entry[user_state_ca[chat_id]]] = text
        user_state_ca[chat_id] += 1
        ask_question_ca(message)

    elif chat_id in user_state_mena:
        if text == "Пропустить":
            user_data_mena[chat_id][fields_for_mena[user_state_mena[chat_id]]] = ""
            user_data_mena_for_post[form_entry[user_state_mena[chat_id]]] = ""
        else:
            user_data_mena[chat_id][fields_for_mena[user_state_mena[chat_id]]] = text
            user_data_mena_for_post[form_entry[user_state_mena[chat_id]]] = text
        user_state_mena[chat_id] += 1
        ask_question_mena(message)



def ask_question_ca(message):
    chat_id = message.chat.id

    if user_state_ca[chat_id] >= len(fields_for_ca):
        bot.send_message(chat_id, 'Спасибо за ваше время. Мы получили все ваши ответы.')
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="На главную")
        keyboard.add(button)
        response = requests.post(url_ca, data=user_data_ca_for_post)
        user_data_ca_for_post.clear()
        if response.status_code == 200:
            print('Форма успешно отправлена')
        else:
            print('Произошла ошибка при отправке формы')
        bot.send_message(chat_id,
                         f'Форма успешно отправлена, вы можете присоединиться к нашему сообществу по этой ссылке: {channel_open_california_chat_link}',
                         reply_markup=keyboard)

        del user_state_ca[chat_id]
    elif fields_for_ca[user_state_ca[chat_id]] == 'Хотели бы Вы стать партнером OpenCA?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Да', 'Нет', 'Не знаю, что мне это даст')
        bot.send_message(chat_id, fields_for_ca[user_state_ca[chat_id]], reply_markup=keyboard)
    elif fields_for_ca[user_state_ca[chat_id]] == 'Какой из форматов встреч нравится и актуален для вас?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Pitch Day и панельная дискуссия с инвесторами',
                     'Проверенная информация, как развиваться в California',
                     'Практика для Вашего бизнеса на стратегических сессиях',
                     'Погружение через бизнес-поездки по региону')
        bot.send_message(chat_id, fields_for_ca[user_state_ca[chat_id]], reply_markup=keyboard)
    elif fields_for_ca[user_state_ca[chat_id]] == 'Телефон для связи':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(chat_id, "Пожалуйста, отправьте ваш номер телефон", reply_markup=keyboard)
    elif fields_for_ca[user_state_ca[chat_id]] == 'Количество человек в Вашей команде?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Пропустить')
        bot.send_message(chat_id, fields_for_ca[user_state_ca[chat_id]], reply_markup=keyboard)
    elif fields_for_ca[user_state_ca[chat_id]] == 'На какие темы Вы хотите выступать?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Пропустить')
        bot.send_message(chat_id, fields_for_ca[user_state_ca[chat_id]], reply_markup=keyboard)
    else:
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, fields_for_ca[user_state_ca[chat_id]], reply_markup=keyboard)

def ask_question_mena(message):
    chat_id = message.chat.id

    if user_state_mena[chat_id] >= len(fields_for_mena):
        bot.send_message(chat_id, 'Спасибо за ваше время. Мы получили все ваши ответы.')
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="На главную")
        keyboard.add(button)
        response = requests.post(url_mena, data=user_data_mena_for_post)
        user_data_mena_for_post.clear()
        if response.status_code == 200:
            print('Форма успешно отправлена')
        else:
            print('Произошла ошибка при отправке формы')
        bot.send_message(chat_id,
                         f'Форма успешно отправлена, вы можете присоединиться к нашему сообществу по этой ссылке: {channel_open_mena_chat_link}',
                         reply_markup=keyboard)

        del user_state_mena[chat_id]
    elif fields_for_mena[user_state_mena[chat_id]] == 'Хотели бы Вы стать партнером OpenMENA?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Да', 'Нет', 'Не знаю, что мне это даст')
        bot.send_message(chat_id, fields_for_mena[user_state_mena[chat_id]], reply_markup=keyboard)
    elif fields_for_mena[user_state_mena[chat_id]] == 'Какой из форматов встреч нравится и актуален для вас?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Pitch Day и панельная дискуссия с инвесторами',
                     'Проверенная информация, как развиваться в MENA',
                     'Практика для Вашего бизнеса на стратегических сессиях',
                     'Погружение через бизнес-поездки по региону')
        bot.send_message(chat_id, fields_for_mena[user_state_mena[chat_id]], reply_markup=keyboard)
    elif fields_for_mena[user_state_mena[chat_id]] == 'Телефон для связи':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(chat_id, "Пожалуйста, отправьте ваш номер телефон", reply_markup=keyboard)
    elif fields_for_mena[user_state_mena[chat_id]] == 'Количество человек в Вашей команде?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Пропустить')
        bot.send_message(chat_id, fields_for_mena[user_state_mena[chat_id]], reply_markup=keyboard)
    elif fields_for_mena[user_state_mena[chat_id]] == 'На какие темы Вы хотите выступать?':
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add('Пропустить')
        bot.send_message(chat_id, fields_for_mena[user_state_mena[chat_id]], reply_markup=keyboard)
    else:
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, fields_for_mena[user_state_mena[chat_id]], reply_markup=keyboard)


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


# Запускаем бота
bot.polling()
