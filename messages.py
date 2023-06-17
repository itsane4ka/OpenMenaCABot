class Messages:
    def __init__(self):
        pass

    def message1(self, first_name):
        message_1 = f"Привет, {first_name}! 🙌 \n\nТы находишься в боте Open MENA и OpenCA - ведущего русскоязычного делового сообщества бизнесменов и инвесторов в MENA и Калифорнии."""
        return message_1

    def message2(self):
        message_2 = "Для начала ВАЖНО подписаться на канал OpenMENA, чтобы получить “Анализ районов MENA”."""
        return message_2

    def message3(self, link):
        message_3 = f"Наш канал: {link[0]}"
        return message_3

    def message4(self):
        message_4 = "Хм.. Не можем найти вашу подписку. Попробуем еще раз?"
        return message_4

    def message5(self):
        message_5 = "Мы собрали большую аналитику по MENA-региону, и она уже доступна вам в прикрепленном файле."
        return message_5

    def message6(self):
        message_6 = "🎊 Welcome to OpenMENA!\n\nНажимайте на интересующий раздел в меню ниже, Вам откроется подробная информация о нас, наших мероприятиях и возможностях для сотрудничества.\n\nЕсли появятся вопросы, Вы всегда можете связаться с менеджером. 🤝"
        return message_6
