from telebot import types

def language():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    eng = types.KeyboardButton('english')
    rus = types.KeyboardButton('русский язык')
    kb.add(eng, rus)
    return kb

def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num = types.KeyboardButton('Отправить номер/Send number', request_contact=True)
    kb.add(num)
    return kb
def loc_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    loc = types.KeyboardButton('Отправить геопозицию/Send location', request_location=True)
    kb.add(loc)
    return kb

def help_button():
    kb = types.InlineKeyboardMarkup(row_width=2)
    podderjka = types.InlineKeyboardButton(text='Служба поддержки/Support service', callback_data='podderjka')
    obrasheniye = types.InlineKeyboardButton(text='Написать обращение/Write on appeal', callback_data='obrasheniye')
    voprosi = types.InlineKeyboardButton(text='Часто задаваемые вопросы/Frequently asked questions (FAQ)', callback_data='voprosi')
    kb.row(podderjka, obrasheniye, voprosi)
    return kb