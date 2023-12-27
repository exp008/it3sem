import telebot
import random
from telebot import types  # для создания кнопок

bot = telebot.TeleBot('6714039906:AAEwA3hzucbbt99zSFYmrc97cEucSImX8kM')


#Создание кнопки после команды Start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_sender = types.KeyboardButton("Скинь Рандомное число")
    markup.add(random_sender)
    bot.send_message(message.chat.id, '<b>Генератор Рандома Активирован</b> (бип-пуп-пиип)', parse_mode='html', reply_markup=markup)


#Отслеживание нажатий кнопки
@bot.message_handler(content_types=['text'])


def get_command(message):
    if message.text == 'Скинь Рандомное число':
        msg = bot.send_message(message.chat.id, 'Введите начало диапазона')
        bot.register_next_step_handler(msg, get_first_number)
    else:
        bot.send_message(message.chat.id, 'Такой команды нет')


#Получение первого числа диапазона
def get_first_number(message):
    try:
        global NUM_first
        NUM_first = int(message.text)
        msg = bot.send_message(message.chat.id, 'Введите конец диапазона')
        bot.register_next_step_handler(msg, get_second_number)
    except ValueError:
        msg = bot.send_message(message.chat.id, 'неверный диапазон')
        bot.register_next_step_handler(msg, get_first_number)


#Получение второго числа диапазона
def get_second_number(message):
    global NUM_second
    NUM_second = int(message.text)
    result(message)                                                          # Вызов функции result(message)


#Вывод результата (рандом)
def result(message):
    bot.send_message(message.chat.id, 'Случайное число:  ' + str(random.randint(NUM_first, NUM_second)))


#Run
bot.polling(none_stop=True)
import telebot
import random
from telebot import types  # для создания кнопок

bot = telebot.TeleBot('6714039906:AAEwA3hzucbbt99zSFYmrc97cEucSImX8kM')


#Создание кнопки после команды Start
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_sender = types.KeyboardButton("Скинь Рандомное число")
    markup.add(random_sender)
    bot.send_message(message.chat.id, '<b>Генератор Рандома Активирован</b> (бип-пуп-пиип)', parse_mode='html', reply_markup=markup)


#Отслеживание нажатий кнопки
@bot.message_handler(content_types=['text'])


def get_command(message):
    if message.text == 'Скинь Рандомное число':
        msg = bot.send_message(message.chat_id, 'Введите начало диапазона')
        bot.register_next_step_handler(msg, get_first_number)
    else:
        bot.send_message(message.chat.id, 'Такой команды нет')


#Получение первого числа диапазона
def get_first_number(message):
    try:
        global NUM_first
        NUM_first = int(message.text)
        msg = bot.send_message(message.chat.id, 'Введите конец диапазона')
        bot.register_next_step_handler(msg, get_second_number)
    except ValueError:
        msg = bot.send_message(message.chat.id, 'неверный диапазон')
        bot.register_next_step_handler(msg, get_first_number)


#Получение второго числа диапазона
def get_second_number(message):
    global NUM_second
    NUM_second = int(message.text)
    msg = bot.send_message(message.chat.id, 'Результат')
    bot.register_next_step_handler(msg, result)


#Вывод результата (рандом)
def result(message):
    bot.send_message(message.chat.id, 'Случайное число:  ' + str(random.randint(NUM_first, NUM_second)))


#Run
bot.polling(none_stop=Tru
