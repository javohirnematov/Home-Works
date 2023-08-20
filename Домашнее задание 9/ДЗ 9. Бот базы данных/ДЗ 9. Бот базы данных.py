import telebot
import sqlite3

bot = telebot.TeleBot('6587646913:AAGF4c9J5cfOoFMwNsOGYoqlWsanr7fUHIs')

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
        id INTEGER
    )""")

    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id={people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, "Такой пользователь уже существует")

@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('user.db')
    cursor = connect.cursor()
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()

bot.polling(non_stop=True)