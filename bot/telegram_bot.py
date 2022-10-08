import telebot
import random
from telebot import types # для указание типов
from collections import defaultdict
import requests

# Создаем бота
print("Initialized")
bot = telebot.TeleBot('5667103443:AAE9RmoqEnj5ENeYvGg6FySft-_dySgBvPc')




# Команда start
@bot.message_handler(commands=["start"])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Роль 1")
    btn2 = types.KeyboardButton("Роль 2")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для вывода новостей!".format(
                         message.from_user), reply_markup=markup)

    # Добавляем две кнопки


messages = ['', '']

# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def func(message):



    if (message.text == "Роль 1" or message.text == "Роль 2"):

        if(message.text == "Роль 1"):
            messages[0] = "score_role_1"
            messages[1] = "Роль 1"
        elif(message.text == "Роль 2"):
            messages[0] = "score_role_2"
            messages[1] = "Роль 2"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Новости")
        btn2 = types.KeyboardButton("Новости по датам")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выберите действие", reply_markup=markup)


    elif (message.text == "Новости"):
        if(messages[0] == "score_role_2" or messages[0] == "score_role_1"):
            res = requests.get("http://37.139.43.52:5000/api/main/" + messages[0] +"/0")
            res = res.json()
            for body_news in res:
                message_news = "НОВОСТИ ДЛЯ " + messages[1].upper() + "\n\n"
                message_news += "📰 Новость: " + body_news[1] + "\n\n Источник: " + body_news[3] + "\n Дата: " +\
                                body_news[4] + "\n Тема: " + body_news[5] + "\n\nОписание: " + body_news[6] +\
                                "\n\n Полную информацию можно посмотреть здесь: " + body_news[2] + "\n\n\n\n\n"
                bot.send_message(message.chat.id, message_news)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Роль 1")
            button2 = types.KeyboardButton("Роль 2")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="Вам нужно выбрать роль", reply_markup=markup)


    elif message.text == "Новости по датам":
        if(messages[0] == "score_role_2" or messages[0] == "score_role_1"):
            bot.send_message(message.chat.id, text="тут будет запрос к апи по датам" + messages[0])
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Роль 1")
            button2 = types.KeyboardButton("Роль 2")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="Вам нужно выбрать роль", reply_markup=markup)


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Роль 1")
        button2 = types.KeyboardButton("Роль 2")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


# Запускаем бота
print("Start")
bot.polling(none_stop=True, interval=0)

