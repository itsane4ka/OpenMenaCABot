import telebot
from telebot import types
from messages import Messages
import random
import requests
from amocrm.v2 import tokens, Contact as _Contact, custom_field, Lead, links

tokens.default_token_manager(
    client_id="6dde3fe6-648b-4f88-9477-5e77655f226b",
    client_secret="hpRgzOS1xDmhn1ZNGFUw3XjJ1wMkWOlSTAp63vW4nFetKRThqmknKAnab7yr2YMZ",
    subdomain="teamopenmenagroup",
    redirect_url="https://go.com",
    storage=tokens.FileTokensStorage(),  # by default FileTokensStoragec
)

#tokens.default_token_manager.init(code="def502000e466751936f8db9088eeddaa238a7341df65821cb8f5a99becb275fec2e9e9bfd520c82a7cf7be80104e7076097465862232f998c88129a2cb5585a8fec7032cded4e92707fe2ffa6fad77e87fcd459817fafb19e3d16f4c9615f2dac134d87c348969be5524550d66c5e30a2d0dabd5467eab35cbc8a37be6efb59f2010f32d1c17ba937eb70a8dc0b8e176d03384f546a9ce660e23a6737d658642af9fcbfafc3c8391534791a5363afb664f5b814bf01eee6a76e4924dedcf2a285db8470c4bbe8d4b25d5462ff78b61c500f0c1f48308f5e6b83aa6ed6e8b2ad8d096739281a5589ebed007bead0dbad7c3f56e9cb9eb7e6fc84ed4d7e76c9cce543d108215293fe343a9a0e12eb1e3f87061f53012f5ec22883fb482ffd955c41c26e362af3fb9e4aa35dd25430bc056244d42e01cdf57b53cab70cc55e4f0ba3fe7699a99e078b190ac2f16bb7393dd2249bf48a54f3b5e21cd902ae2f4f8113d514148cc14e4390981d9e1e12ddb5412439ac01dd5a793e372b3f135aea62791bc6e8cac7bdb2fea6a45a49220164088edd3840585d7d16c9a7c6a67302579032833f05b7960c24cc569cef88c10527bc478cbe68a709665b19d4d7a2a95fd29a937a36235caae909f044e44bc2c6805a24117db30cd1d5574357970f", skip_error=True)


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

user_state_ca, user_state_mena, user_data_ca, user_data_mena = {}, {}, {}, {},

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


# form_entry = [
#     'entry.91462916',
#     'entry.630533396',
#     'entry.2039931063',
#     'entry.1318559028',
#     'entry.1254544746',
#     'entry.191036165',
#     'entry.854259575',
#     'entry.1448253998',
#     'entry.729755307',
#     'entry.601340499',
#     'entry.292760203',
#     'entry.1874047276',
#     'entry.1566950839',
#     'entry.104522551',
#     'entry.281659691',
#     'entry.2132372300',
#     'entry.1885107982',
# ]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):

    #lead = Lead.objects.create()
    #print(lead.id)
    #lead.save()


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
    chat_id = message.chat.id
    if chat_id in user_state_ca and fields_for_ca[user_state_ca[chat_id]] == 'Телефон для связи':
        user_data_ca[chat_id][fields_for_ca[user_state_ca[chat_id]]] = message.contact.phone_number
        user_state_ca[chat_id] += 1
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, fields_for_ca[user_state_ca[chat_id]],
                         reply_markup=keyboard)
    elif chat_id in user_state_mena and fields_for_mena[user_state_mena[chat_id]] == 'Телефон для связи':
        user_data_mena[chat_id][fields_for_mena[user_state_mena[chat_id]]] = message.contact.phone_number
        user_state_mena[chat_id] += 1
        keyboard = types.ReplyKeyboardRemove()
        bot.send_message(chat_id, fields_for_mena[user_state_mena[chat_id]],
                         reply_markup=keyboard)
    else:
        contact = message.contact
        phone_number = contact.phone_number
        first_name = contact.first_name
        last_name = contact.last_name or ""

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


    # second code

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
            # user_data_ca_for_post[form_entry[user_state_ca[chat_id]]] = ""
        else:
            user_data_ca[chat_id][fields_for_ca[user_state_ca[chat_id]]] = text
            # user_data_ca_for_post[form_entry[user_state_ca[chat_id]]] = text
        user_state_ca[chat_id] += 1
        ask_question_ca(message)

    elif chat_id in user_state_mena:
        if text == "Пропустить":
            user_data_mena[chat_id][fields_for_mena[user_state_mena[chat_id]]] = ""
        else:
            user_data_mena[chat_id][fields_for_mena[user_state_mena[chat_id]]] = text
        user_state_mena[chat_id] += 1
        ask_question_mena(message)

    else:
        bot.send_message(chat_id, "Я не понимаю такой команды.")


def ask_question_ca(message):
    chat_id = message.chat.id

    if user_state_ca[chat_id] >= len(fields_for_ca):
        bot.send_message(chat_id, 'Спасибо за ваше время. Подождите пару секунд для обработки ответов!')
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="На главную")
        keyboard.add(button)
        print(user_data_ca)
        send_to_crm(is_ca=True, chat_id=chat_id)

        # response = requests.post(url_ca, data=user_data_ca_for_post)
        # if response.status_code == 200:
        #     print('Форма успешно отправлена')
        # else:
        #     print('Произошла ошибка при отправке формы')
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
        bot.send_message(chat_id, 'Спасибо за ваше время. Подождите пару секунд для обработки ответов!')
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button = types.KeyboardButton(text="На главную")
        keyboard.add(button)
        print(user_data_mena)
        send_to_crm(is_ca=False, chat_id=chat_id)
        # response = requests.post(url_mena, data=user_data_mena_for_post)
        # if response.status_code == 200:
        #     print('Форма успешно отправлена')
        # else:
        #     print('Произошла ошибка при отправке формы')
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

    with open('resources/doc.pdf', 'rb') as pdf:
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

    photo = open('resources/openmena.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message7(), reply_markup=keyboard)

    photo.close()


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

    photo = open('resources/pitch.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message12(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


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

    photo = open('resources/academy.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message13(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


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

    photo = open('resources/trip.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message14(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


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

    photo = open('resources/stratses.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message15(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


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

    photo = open('resources/amasession.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message16(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


# Send the analysis info
def send_message_4_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подать заявку")
    button3 = types.KeyboardButton(text="Стать партнером")
    button4 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button3, button4)

    bot.send_message(chat_id, mes.message9(), reply_markup=keyboard)


# Send the analysis info
def send_message_5_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Подать заявку")
    button2 = types.KeyboardButton(text="Стать участником")
    button3 = types.KeyboardButton(text="OpenCalifornia")
    button4 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button3, button4)

    photo = open('resources/partnership.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message10(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


# Send the analysis info
def send_message_6_ticket(chat_id):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text="Стать участником OpenCA")
    button2 = types.KeyboardButton(text="Kанал OpenCalifornia")
    button4 = types.KeyboardButton(text="На главную")
    keyboard.add(button1, button2, button4)

    photo = open('resources/openca.png', 'rb')  # Opening the image file

    bot.send_photo(chat_id, photo, caption=mes.message11(), reply_markup=keyboard)

    photo.close()  # Closing the image file after sending


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
    #bot.send_contact(chat_id, phone_number, first_name, last_name)

    bot.send_message(chat_id, text="@openMENA_admin")




def send_to_crm(is_ca: bool, chat_id):
    user_data = user_data_ca if is_ca else user_data_mena

    class Contact(_Contact):
        custom1 = custom_field.TextCustomField("Телефон")
        custom2 = custom_field.TextCustomField("Ваш Telegram")
        custom3 = custom_field.TextCustomField("Email")
        custom4 = custom_field.TextCustomField("В какой стране Вы живете?")
        custom5 = custom_field.TextCustomField("Опишите деятельность Вашей компании?")
        custom6 = custom_field.TextCustomField("Регион присутствия (в том числе планируемый) Вашей компании?")
        custom7 = custom_field.TextCustomField("Как называется Ваша компания?")
        custom8 = custom_field.TextCustomField("Ссылка на сайт компании")
        custom9 = custom_field.TextCustomField("Годовой оборот Вашей компании?")
        custom10 = custom_field.TextCustomField("Количество человек в Вашей команде?")
        custom11 = custom_field.TextCustomField("Дополнительные направления бизнеса, которые Вы развиваете?")
        custom12_ca = custom_field.TextCustomField("Вы хотите стать спикером на мероприятиях OpenCA?")
        custom12_mena = custom_field.TextCustomField("Вы хотите стать спикером на мероприятиях OpenMENA?")
        custom13 = custom_field.TextCustomField("На какие темы Вы хотите выступать?")
        custom14_ca = custom_field.TextCustomField("Хотели бы Вы стать партнером OpenCA?")
        custom14_mena = custom_field.TextCustomField("Хотели бы Вы стать партнером OpenMENA?")
        custom15_ca = custom_field.TextCustomField("Цель участия в OpenCA")
        custom15_mena = custom_field.TextCustomField("Цель участия в OpenMENA")
        custom16 = custom_field.TextCustomField("Какой из форматов встреч нравится и актуален для вас?")

    lead = Lead.objects.create()
    lead.save()

    contact = Contact.objects.create(name=user_data[chat_id]["Имя Фамилия"])
    contact.custom1 = user_data[chat_id]["Телефон для связи"]
    contact.custom2 = user_data[chat_id]["Ваш Telegram"]
    contact.custom3 = user_data[chat_id]["Email"]
    contact.custom4 = user_data[chat_id]["В какой стране Вы живете?"]
    contact.custom5 = user_data[chat_id]["Опишите деятельность Вашей компании?"]
    contact.custom6 = user_data[chat_id]["Регион присутствия (в том числе планируемый) Вашей компании?"]
    contact.custom7 = user_data[chat_id]["Как называется Ваша компания?"]
    contact.custom8 = user_data[chat_id]["Ссылка на сайт компании"]
    contact.custom9 = user_data[chat_id]["Годовой оборот Вашей компании?"]
    contact.custom10 = user_data[chat_id]["Количество человек в Вашей команде?"]
    contact.custom11 = user_data[chat_id]["Дополнительные направления бизнеса, которые Вы развиваете?"]
    contact.custom13 = user_data[chat_id]["На какие темы Вы хотите выступать?"]
    contact.custom16 = user_data[chat_id]["Какой из форматов встреч нравится и актуален для вас?"]

    if is_ca:
        contact.custom12_ca = user_data[chat_id]["Вы хотите стать спикером на мероприятиях OpenCA?"]
        contact.custom14_ca = user_data[chat_id]["Хотели бы Вы стать партнером OpenCA?"]
        contact.custom15_ca = user_data[chat_id]['Цель участия в OpenCA']
    else:
        contact.custom12_mena = user_data[chat_id]["Вы хотите стать спикером на мероприятиях OpenMENA?"]
        contact.custom14_mena = user_data[chat_id]["Хотели бы Вы стать партнером OpenMENA?"]
        contact.custom15_mena = user_data[chat_id]["Цель участия в OpenMENA"]

    contact.save()
    links.LinksInteraction().link(lead, contact)
    lead.save()
    if is_ca:
        user_data_ca.clear()
    else:
        user_data_mena.clear()

# Запускаем бота
bot.polling()