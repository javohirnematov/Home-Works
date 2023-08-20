import telebot, user_buttons as ub, datebase as db
from telebot.types import ReplyKeyboardRemove as remove
from geopy import Nominatim

bot = telebot.TeleBot('6307341839:AAFwtiu7PWvu5qWhBr1jLFJLHUnCTJH1CKk')
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')

lang = {}
eng = {'registration': "Greetings! Let's start registration, write your name",
       'number': 'Great! Now send the number',
       'location': 'Now send the location!',
       'button_number': 'Send your contact via the button!',
       'button_location': 'Submit your location via the button',
       'complete_registration': 'You have successfully registered!',
       'hello': ', greetings! For information, enter "/help"',
       'hello_new': 'For help, enter "/help"',
       'help_me': 'Choose what kind of help you need!',
       'support_service': 'support:',
       'help_number': 'Call this number +998997269811',
       'appeal': 'write an appeal',
       'write_an_appeal': 'Write an appeal https://t.me/java_nematov',
       'questions': 'frequently asked questions (FAQ)',
       'answers_on_questions': 'Try to find your question on this link: https://otvet.mail.ru/',
       'sorry': 'Sorry, this operation does not work at the moment. Contact Support'}

rus = {'registration': 'Приветствую вас! Начнем регистрацию, напишите свое имя',
       'number': 'Отлично! А теперь отправьте номер',
       'location': 'А теперь отправьте локацию!',
       'button_number': 'Отправьте свой контакт через кнопку!',
       'button_location': 'Отправьте свою локацию через кнопку!',
       'complete_registration': 'Вы успешно зарегистрировались!',
       'hello': 'Приветствую вас! Для получения информации введите "/help"',
       'hello_new': 'Для получения справочной информации введите "/help"',
       'help_me': 'Выберите какой вид помощи вам нужен!',
       'support_service': 'служба поддержки:',
       'help_number': 'Позвоните по данному номеру +998997269811',
       'appeal': 'написать обращение',
       'write_an_appeal': 'Написать обращение https://t.me/java_nematov',
       'questions': 'часто задаваемые вопросы',
       'answers_on_questions': 'Попробуйте найти интересующий вас вопрос по данной ссылке: https://otvet.mail.ru/',
       'sorry': 'Извините на данный момент эта операция не работает. Обратитесь в службу поддержки'}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Choice language / Выберите язык', reply_markup=ub.language())
    bot.register_next_step_handler(message, choice_language)

def choice_language(message):
    global lang
    if message.text == 'english':
        lang = eng
    elif message.text == 'русский язык':
        lang = rus
    else:
        bot.send_message(message.from_user.id, 'Choice language / Выберите язык', reply_markup=ub.language())
        bot.register_next_step_handler(message, choice_language)

    check_user = db.name(message.from_user.id)
    if check_user:
        bot.send_message(message.from_user.id, lang['hello'], reply_markup=remove())
    else:
        bot.send_message(message.from_user.id, lang['registration'], reply_markup=remove())
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_name = message.text
    bot.send_message(message.from_user.id, lang['number'], reply_markup=ub.num_button())
    bot.register_next_step_handler(message, get_num, user_name)

def get_num(message, user_name):
    if message.contact:
        user_num = message.contact.phone_number
        bot.send_message(message.from_user.id, lang['location'], reply_markup=ub.loc_button())
        bot.register_next_step_handler(message, get_loc, user_name, user_num)
    else:
        bot.send_message(message.from_user.id, lang['button_number'])
        bot.register_next_step_handler(message, get_num, user_name)

def get_loc(message, user_name, user_num):
    if message.location:
        user_loc = geolocator.reverse(f'{message.location.longitude}, {message.location.latitude}')
        db.register(message.from_user.id, user_name, user_num, user_loc)
        bot.send_message(message.from_user.id, lang['complete_registration'], reply_markup=remove())
        bot.send_message(message.from_user.id, lang['hello_new'], reply_markup=remove())
    else:
        bot.send_message(message.from_user.id, lang['button_location'])
        bot.register_next_step_handler(message, get_loc, user_name, user_num)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, lang['help_me'], reply_markup=ub.help_button())

@bot.callback_query_handler(lambda call: call.data in ['podderjka', 'obrasheniye', 'voprosi'])
def cart_handle(call):
    if call.data == 'podderjka':
        bot.edit_message_text(lang['help_number'], call.message.chat.id, call.message.message_id, reply_markup=ub.help_button())
    elif call.data == 'obrasheniye':
        bot.edit_message_text(lang['write_an_appeal'], call.message.chat.id, call.message.message_id, reply_markup=ub.help_button())
    elif call.data == 'voprosi':
        bot.edit_message_text(lang['answers_on_questions'], call.message.chat.id, call.message.message_id, reply_markup=ub.help_button())
    else:
        bot.edit_message_text(lang['sorry'], chat_id=chat_id, message_id=call.message.message_id, reply_markup=ub.help_button())

bot.polling(non_stop=True)

