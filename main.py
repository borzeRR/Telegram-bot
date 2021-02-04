import telebot
import re
import math
from telebot import types

bot = telebot.TeleBot("1613118082:AAFAOU2iiZDUbd2qjA5G5Kovv4D3ZufjFyo")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text == '/start':
        start_message = '''Здравствуйте, это математической бот. Он умеет решать множество уравнений и выражений. 
Для того чтобы узнать, как именно писать то или иное выражение, нажмите на кнопку "Справка"'''
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        help_button = types.KeyboardButton('Справка')
        markup.add(help_button)
        bot.send_message(message.chat.id, start_message, reply_markup=markup)
        keyboard()


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Справка':
        bot.reply_to(message, 'Квадратное уравнение: ax^2 + bx + c')
    elif re.search(r'(\d*)x\^2\s*\+\s*(\d*)x\s*\+\s*(\d*)', message.text):
        match = re.search(r'(\d*)x\^2\s*\+\s*(\d*)x\s*\+\s*(\d*)', message.text)
        a = int(match.group(1))
        b = int(match.group(2))
        c = int(match.group(3))
        d = (b ** 2) - 4 * a * c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            bot.reply_to(message, f'{x1};{x2}')
        elif d == 0:
            x1 = -b / (2 * a)
            bot.reply_to(message, x1)
        elif d < 0:
            bot.reply_to(message, 'Дискриминант меньше 0, уравнение не имеет корней')
    else:
        bot.reply_to(message, 'Извините, но я, к сожалению, вас не понимаю. Воспользуйтесь кнопкой "Reference".')


def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    help_button = types.KeyboardButton('Справка')
    markup.add(help_button)
    return markup


if __name__ == '__main__':
    bot.polling(none_stop=True)
