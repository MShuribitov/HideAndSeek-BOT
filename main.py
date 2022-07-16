import telebot
from telebot import types
from database.db import *

TOKEN = "5522146184:AAFM2c2k7OIsJSBuAH2ibBhMFQFDJsSGHhM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.username}")
@bot.message_handler(commands=['game'])
def start_game(message):
    CreateTable(message.from_user.id, message.from_user.username, message.chat.id)
    bot.send_message(message.chat.id, "Игра успешно началась")
    bot.send_message(message.chat.id, "Hello!")

bot.polling(none_stop=True)