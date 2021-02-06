import telebot
import re
import math
from telebot import types

bot = telebot.TeleBot("1613118082:AAFAOU2iiZDUbd2qjA5G5Kovv4D3ZufjFyo")

quadratic_rematch = r'(\-?\d*)x\^2\s*((\+|\-)\s*\d*)x\s*((\+|\-)\s*\d*)(\s*\=\s*0)?'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text == '/start':
        start_message = '''Здравствуйте, это математической бот. Он умеет решать множество уравнений и выражений. 
Для того чтобы узнать, как именно писать то или иное выражение, нажмите на кнопку "Справка"'''
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        help_button = types.KeyboardButton('Справка')
        markup.add(help_button)
        bot.send_message(message.chat.id, start_message, reply_markup=markup)
        return markup


@bot.message_handler(content_types=['text'])
def check_message(message):
    if message.text == 'Справка':
        bot.reply_to(message, 'Квадратное уравнение: ax^2 + bx + c')
    elif is_quadratic(message):
        quadratic_solve(message)
    else:
        bot.reply_to(message, 'Извините, но я, к сожалению, вас не понимаю. Воспользуйтесь кнопкой "Reference".')


def is_quadratic(message):
    if re.search(quadratic_rematch, message.text):
        return True
    else:
        return False


def quadratic_solve(message):
    match = re.search(quadratic_rematch, message.text)
    a_string = match.group(1).split()
    b_string = match.group(2).split()
    c_string = match.group(4).split()
    a = int(''.join(a_string))
    b = int(''.join(b_string))
    c = int(''.join(c_string))
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


if __name__ == '__main__':
    bot.polling(none_stop=True)
