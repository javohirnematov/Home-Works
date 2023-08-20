import requests
import telebot, converter_start as cs

bot = telebot.TeleBot('6370278463:AAETRU_2TCtvr48IRwjDKqmuL7Et5SOoJQ4')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Добро пожаловать, выберите действие?',
                     reply_markup=cs.choice_button())
    bot.register_for_reply(message, curs_convert)

@bot.message_handler(content_types=['text'])
def curs_convert(message):
    response = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/')
    if message.text == 'курс валют':
        usd = float(response.json()[0]['Rate'])
        bot.send_message(message.from_user.id, f'Курс американского доллар к сумму равен {usd}')
        eur = float(response.json()[1]['Rate'])
        bot.send_message(message.from_user.id, f'Курс европейской валюты евро к сумму равен {eur}')
        rub = float(response.json()[2]['Rate'])
        bot.send_message(message.from_user.id, f'Курс российского рубля к сумму равен {rub}')
    elif message.text == 'конвертация':
        bot.send_message(message.from_user.id, 'Введите сумму для конвертации в узбекских суммах')
        bot.register_next_step_handler(message, convert)
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял')

def convert(message):
    response = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/')
    summa = int(message.text)
    usd = float(response.json()[0]['Rate'])
    convert_usd = summa / usd
    bot.send_message(message.from_user.id, f'{summa} сумм = {convert_usd} американским долларам')
    eur = float(response.json()[1]['Rate'])
    convert_eur = summa / eur
    bot.send_message(message.from_user.id, f'{summa} сумм = {convert_eur} евро')
    rub = float(response.json()[2]['Rate'])
    convert_rub = summa / rub
    bot.send_message(message.from_user.id, f'{summa} сумм = {convert_rub} рублей')

bot.polling(none_stop=True)
