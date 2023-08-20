import telebot, database_delivery_bot as db, buttons_delivery_bot as bt
from telebot.types import ReplyKeyboardRemove as remove
from geopy import Nominatim

bot = telebot.TeleBot('6365556857:AAG_N8bqDYddWLKlVSkvbKwtsIglfIksGKA')
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

users = {}
leng = {}
ru = {'start': 'Добро пожаловать!',
      'main': 'Выберите пункт меню',
      'num': 'Отлично! А теперь отправьте номер!',
      'loc': 'А теперь отправьте локацию!',
      'but': 'Отправьте через кнопку!',
      'reg_s': 'Вы успешно зарегистрировались!',
      'gret': 'Приветствую вас! Начнем регистрацию, напишите свое имя',
      'to_cart': 'Ваш товар был добавлен в корзину! Хотите заказать что-то еще?',
      'to_order': 'Заказ был оформлен и скоро будет доставлен! Желаете заказать что-то еще?',
      'clean': 'Корзина очищена! Желаете что-то еще?',
      'quantity': 'Выберите количество'}
eng = {'start': 'Welcome!',
       'main': 'Select a menu item',
       'num': 'Great! And now send the number!',
       'loc': 'And now send the location!',
       'but': 'Send via the button!',
       'reg_s': 'You have successfully registered!',
       'gret': 'Greetings to you! Let"s start the registration, write your name',
       'to_cart': 'Your product has been added to the cart! Do you want to order something else?',
       'to_order': 'The order has been placed and will be delivered soon! Would you like to order something else?',
       'clean': 'The cart is cleared! Would you like something else?',
       'quantity': 'Select the quantity'}

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, 'Выберите язык/Choose language(ru-eng)', reply_markup=remove())
    bot.register_next_step_handler(message, language)

def language(message):
    global leng
    if message.text == 'ru':
        leng = ru
    elif message.text == 'eng':
        leng = eng
    else:
        bot.send_message(user_id, 'Выберите язык/Choose language(ru-eng)')
        bot.register_next_step_handler(message, language)

    check_user = db.checker(user_id)
    if check_user:
        products = db.get_pr_name_id()                                                                                  #Выводит список продуктов из БД
        bot.send_message(user_id, leng['start'], reply_markup=remove())
        bot.send_message(user_id, leng['main'], reply_markup=bt.main_menu_buttons(products))
    else:
        bot.send_message(user_id, leng['gret'], reply_markup=remove())
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_name = message.text
    bot.send_message(user_id, leng['num'], reply_markup=bt.num_button())
    bot.register_next_step_handler(message, get_num, user_name)

def get_num(message, user_name):
    if message.contact:
        user_num = message.contact.phone_number
        bot.send_message(user_id, leng['loc'], reply_markup=bt.loc_button())
        bot.register_next_step_handler(message, get_loc, user_name, user_num)
    else:
        bot.send_message(user_id, leng['but'])
        bot.register_next_step_handler(message, get_num, user_name)

def get_loc(message, user_name, user_num):
    if message.location:
        user_loc = geolocator.reverse(f'{message.location.longitude}, {message.location.latitude}')
        db.register(user_id, user_name, user_num, user_loc)
        bot.send_message(user_id, leng['reg_s'])
        products = db.get_pr_name_id()
        bot.send_message(user_id, leng['main'], reply_markup=bt.main_menu_buttons(products))
    else:
        bot.send_message(user_id, leng['but'])
        bot.register_next_step_handler(message, get_loc, user_name, user_num)

@bot.callback_query_handler(lambda call: call.data in ['back', 'to_cart', 'increment', 'decrement'])
def get_user_count(call):
    chat_id = call.message.chat.id
    if call.data == 'increment':
        count = users[chat_id]['pr_amount']
        users[chat_id]['pr_amount'] += 1
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=bt.choose_product_count(count, 'increment'))
    elif call.data == 'decrement':
        count = users[chat_id]['pr_amount']
        users[chat_id]['pr_amount'] -= 1
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=bt.choose_product_count(count, 'decrement'))
    elif call.data == 'back':
        products = db.get_pr_name_id()
        bot.edit_message_text(leng['main'], chat_id=chat_id, message_id=call.message.message_id, reply_markup=bt.main_menu_buttons(products))
    elif call.data == 'to_cart':
        products = db.get_pr_name_id()
        product_count = users[chat_id]['pr_amount']
        print(chat_id)
        print(users[chat_id])
        print(users[chat_id]['pr_amount'])
        user_total = products[0][3] * product_count
        user_product = db.get_pr_name(users[chat_id]['pr_name'])
        db.add_to_cart(chat_id, user_product[0], product_count, user_total)
        bot.edit_message_text(leng['to_cart'], chat_id=chat_id, message_id=call.message.message_id, reply_markup=bt.main_menu_buttons(products))

@bot.callback_query_handler(lambda call: call.data in ['cart', 'order', 'clear', 'back'])
def cart_handle(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    products = db.get_pr_name_id()
    if call.data == 'clear':
        db.del_cart(user_id)
        bot.edit_message_text(leng['clean'], chat_id=chat_id, message_id=message_id, reply_markup=bt.main_menu_buttons(products))
    elif call.data == 'order':
        db.del_cart(user_id)
        bot.edit_message_text(leng['to_order'], chat_id=chat_id, message_id=message_id, reply_markup=bt.main_menu_buttons(products))
    elif call.data == 'back':
        bot.edit_message_text(leng['main'], chat_id=chat_id, message_id=call.message.message_id, reply_markup=bt.main_menu_buttons(products))
    elif call.data == 'cart':
        text = db.show_cart(user_id)
        bot.edit_message_text(f'Корзина/Cart:\nТовар/Product: {text[0]}\nКоличество/Quantity: {text[1]}\nИтого/Total: {text[2]}', chat_id=chat_id, message_id=message_id, reply_markup=bt.cart_buttons())

@bot.callback_query_handler(lambda call: int(call.data) in db.get_pr_id())
def get_user_product(call):
    chat_id = call.message.chat.id
    users[user_id] = {'pr_name': call.data, 'pr_amount': 1}
    message_id = call.message.message_id
    bot.edit_message_text(leng['quantity'], chat_id=chat_id, message_id=message_id, reply_markup=bt.choose_product_count())

bot.polling(non_stop=True)