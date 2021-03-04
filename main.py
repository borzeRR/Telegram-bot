import telebot
import re
import math
from telebot import types

bot = telebot.TeleBot("1613118082:AAFAOU2iiZDUbd2qjA5G5Kovv4D3ZufjFyo")

quadratic_rematch = r'^(\-?\d*\.?\d*)x\^2\s*((\+|\-)\s*\d*\.?\d*)x\s*((\+|\-)\s*(\d*\.?\d*))?(\s*\=\s*0)?'


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
    try:
        c_string = match.group(4).split()
        c = float(''.join(c_string))
    except AttributeError:
        c = 0
    if len(a_string) == 0:
        a = 1
    else:
        if any(map(str.isdigit, a_string[0])) is False and '-' not in a_string:
            a = 1
        elif any(map(str.isdigit, a_string[0])) is False and '-' in a_string:
            a = -1
        else:
            a = float(''.join(a_string))
    if len(b_string) == 1 and b_string[0] == '-':
        b = -1
    elif len(b_string) == 1 and b_string[0] == '+':
        b = 1
    else:
        b = float(''.join(b_string))
    d = (b ** 2) - 4 * a * c
    print(a, b, c, d)
    print(math.sqrt(d))
    print(math.sqrt(d) * math.sqrt(d))
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if math.sqrt(d) * math.sqrt(d) == d:
            bot.reply_to(message, f'{x1} ; {x2}')
        else:
            bot.reply_to(message, f'{-b} + √{d}; {-b} - √{d}')
    elif d == 0:
        x1 = -b / (2 * a)
        bot.reply_to(message, x1)
    elif d < 0:
        bot.reply_to(message, 'Дискриминант меньше 0, уравнение не имеет корней')


if __name__ == '__main__':
    bot.polling(none_stop=True)
