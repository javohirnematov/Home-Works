import requests
import telebot, converter_start as cs

bot = telebot.TeleBot('6370278463:AAETRU_2TCtvr48IRwjDKqmuL7Et5SOoJQ4')

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, 'Добро пожаловать, выберите действие?', reply_markup=cs.choice_button())
    bot.register_for_reply(message, curs_convert)
@bot.message_handler(content_types=['text'])
def curs_convert(message):
    if message.text.lower == 'Курсы валют':
        bot.send_message(user_id, 'Выберите пожалуйста валюту', reply_markup=cs.vibor_button())
        bot.register_next_step_handler(message, curs)
    elif message.text.lower == 'Конвертация':
        bot.send_message(user_id, 'Выберите вид конвертации,', reply_markup=cs.convert_button())
        bot.register_next_step_handler(message, convert)

def curs(message):
    response = requests.get("https://cbu.uz/ru/arkhiv-kursov-valyut/json/")
    if message.text.lower() == 'USD':
        usd = response.json()[0]['Rate']
        bot.send_message(user_id, f'Курс американского доллар к сумму равен {usd}')
    elif message.text.lower() == 'EUR':
        eur = response.json()[1]['Rate']
        bot.send_message(user_id, f'Курс европейской валюты евро к сумму равен {eur}')
    elif message.text.lower == 'RUB':
        rub = response.json()[2]['Rate']
        bot.send_message(user_id, f'Курс российского рубля к сумму равен {rub}')
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял')

def convert(message):
    response = requests.get("https://cbu.uz/ru/arkhiv-kursov-valyut/json/")
    if message.text.lower == 'USD/UZB':
        summa = bot.send_message(user_id, 'Введите сумму для конвертации в доллар')
        usd = response.json()[0]['Rate']
        convert = summa / usd
        bot.send_message(user_id, f'{summa} сумм = {convert} американским долларам')
    elif message.text.lower() == 'EUR/UZB':
        summa = bot.send_message(user_id, 'Введите сумму для конвертации в евро')
        eur = response.json()[1]['Rate']
        convert = summa / eur
        bot.send_message(user_id, f'{summa} сумм = {convert} евро')
    elif message.text.lower == 'RUB/UZB':
        summa = bot.send_message(user_id, 'Введите сумму для конвертации в рубли')
        rub = response.json()[2]['Rate']
        convert = summa / rub
        bot.send_message(user_id, f'{summa} сумм = {convert} рублей')
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял')

bot.polling(none_stop=True)