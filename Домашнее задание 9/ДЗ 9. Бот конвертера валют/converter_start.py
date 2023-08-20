import telebot
from telebot import types
def choice_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kurs = types.KeyboardButton('курс валют')
    convertation = types.KeyboardButton('конвертация')
    kb.add(kurs, convertation)
    return kb

