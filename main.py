import telebot
import random

greetings = ['Привет', 'Дарова', 'Здравствуй', 'Доброе утро', 'Добрый день']
farewells = ['Пока', 'До свидания', 'Спокойной ночи']

bot = telebot.TeleBot("1529363822:AAF2LQ2WqMC5zPT2kPf82SRlnNcFvMp2EDo")


@bot.message_handler(command='start')
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text in greetings:
        bot.reply_to(message, random.choice(greetings) + '!')
    elif message.text in farewells:
        bot.reply_to(message, random.choice(farewells) + '!')
    elif message.text == 'Как дела?':
        bot.reply_to(message, 'Хорошо. Как у тебя?')
    else:
        bot.reply_to(message, 'Извините, но я, к сожалению, вас не понимаю :(')


bot.polling()
