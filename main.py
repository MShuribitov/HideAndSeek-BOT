import telebot
from telebot import types
from database.db import DataBase

TOKEN = "5522146184:AAFM2c2k7OIsJSBuAH2ibBhMFQFDJsSGHhM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.username}")
@bot.message_handler(commands=['game'])
def start_game(message):
    DataBase(message.chat.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    join = types.InlineKeyboardButton("✅ Войти", callback_data="join")
    markup.add(join)
    bot.send_message(message.chat.id, "⚠️ Начался набор игроков", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "join":
            DataBase.adduser(call.message.chat.id, call.from_user.id, call.from_user.username)

bot.polling(none_stop=True)