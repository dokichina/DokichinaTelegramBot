#Импорт необходимых модулей
import telebot
import random
import time
from telebot import types
import os
import ctypes
import pyautogui as pag

#Рандомные ответы на сообщения
random_otveti = ['че ты пукнул', 'не пон', 'пон',
                 'и што', 'мм..чееел', 'сам такой',
                 'а мама говорила..😓', 'я тоже', 'у миня нит праблим краме маей башки😖😓',
                 'я тебе глаз на попку натяну)','и что боже эм..', 'ай вона лив вона лив',
                 'ты кто', 'у меня альцгеймер кстати у меня альцгеймер', 'all my friends a toxic...',
                 'ты чтоли из этих...людей чтоли?', 'ну..ладно', 'ахахаха смешно(нет)', 'и чо?!?!',
                 'emae kak raskladky perekluchit?', 'че тебе норм то?', 'ага, ага..', 'ерор404.пажалуста не пишите мне',
                 'класс.', 'а вы с ним похожи...', 'ха, ботик какой-то', 'откуда ты...знаешь..']

random_kakdela = ['я тебе друг чтоле!?!', 'норм', 'все плохо,я дед инсайд', 'чел, какие дела у бота?', 'сру сижу', 'У меня все отлично, а у Вас как?']

random_hello = ['Приветствую дорогой друг!', 'Хай', 'Доброго времени суток', 'О, какие люди,привет!', 'СКОКА ЛЕТ СКОКА ЗИМ!! ЗДРАСТЕЕ']

random_zhiza = ['и вправду жиза', '-я даун\n-жиза', 'согл', 'бывает', 'хм..ну ладно..']

random_hz = ['правильнее будет написать "не знаю"', 'жиза', 'правильнее будет написать "не известно"', 'правильнее будет написать "не имею такой информации"',]

#ТОКЕН и различные переменные
bot = telebot.TeleBot('YOUR TOKEN')
send_time = lambda x: time.strftime("%H:%M:%S", time.localtime(x))

#####################################

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'{random.choice(random_hello)}')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, f'Привет,я бот Семён и вот что я могу(плагиатим алису)\n'
                                      f'Создатель: @monyice'
                                      f'\nВ этот день бот зароботал впервые: 28 апреля 2022 года'
                                      f'\nТо, без чего меня бы не сделали:YouTube,Github,Algoritmika и Хабр'
                                      f'\nНаписан в PyCharm на языке Путхон(Python)')

#####################################

@bot.message_handler(commands=['son'])
def son(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сообщение на ПК[CREATOR FUNC]")
    btn2 = types.KeyboardButton("Сменить обои на ПК[CREATOR FUNC]")
    markup.add(btn1, btn2)
    send_time_realize = send_time(message.date)
    send_time_hours = int((send_time_realize[0:2]))
    def otveti_hours(send_time_hours):
        if send_time_hours > 0 and send_time_hours < 6:
            return 'Доброй ночи'
        elif send_time_hours > 6 and send_time_hours < 12:
            return 'Доброе утро'
        elif send_time_hours > 12 and send_time_hours < 18:
            return 'Добрый день'
        else:
            return 'Добрый вечер'
    bot.send_message(message.chat.id, f'{otveti_hours(send_time_hours)}, {message.chat.first_name}\nВот что может пригодиться', reply_markup=markup)



@bot.message_handler(content_types=['text', 'photo'])
def func(message):
    if message.text == 'Сообщение на ПК[CREATOR FUNC]':
        def next_message_sending(message):
            try:
                pag.alert(message.text, "Сообщение")
            except Exception:
                bot.send_message(message.chat.id, "Что-то пошло не так...")

        msg = bot.send_message(message.chat.id, "Введите ваше сообщение, которое желаете вывести на экран.")
        bot.register_next_step_handler(msg, next_message_sending)
    elif message.text == 'Сменить обои на ПК[CREATOR FUNC]':
        def next_wallpaper(message):
            file = message.photo[-1].file_id
            file = bot.get_file(file)
            dfile = bot.download_file(file.file_path)

            with open("image.jpg", "wb") as img:
                img.write(dfile)

            path = os.path.abspath("image.jpg")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

        msg = bot.send_message(message.chat.id, "Отправьте картинку")
        bot.register_next_step_handler(msg, next_wallpaper)

    elif message.text == 'жиза' or message.text == 'Жиза' or message.text == 'жиз' or message.text == 'Жиз':
        bot.send_message(message.chat.id, f'{random.choice(random_zhiza)}')
    elif message.text == 'привет' or message.text == 'Привет' or message.text == 'жиз' or message.text == 'Жиз':
        bot.send_message(message.chat.id, f'{random.choice(random_zhiza)}')
    elif message.text == 'как дела?' or message.text == 'как дела' or message.text == 'как ты?':
        bot.send_message(message.chat.id, f'{random.choice(random_kakdela)}')
    else:
        bot.send_message(message.chat.id, f'{random.choice(random_otveti)}')

##############################

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)
