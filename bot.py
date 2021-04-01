import telebot
from telebot import types
import config
from questions import questMas
from stickers import stickers

bot = telebot.TeleBot(config.token)
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
button1 = types.KeyboardButton('ЕГЭ🇷🇺')
button2 = types.KeyboardButton('Таблица лидеров🏆')
button3 = types.KeyboardButton('Оставить отзыв')
keyboard1.add(button1, button2, button3)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, вы попали на ЕГЭ по аниме, что будете делать?', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def exam(message):
    answer = types.InlineKeyboardMarkup(row_width=2)
    que_num = 1
    for index, ans in enumerate(questMas[que_num].answers):
        answer.add(types.InlineKeyboardButton(ans, callback_data=str(index)))
    bot.send_photo(message.chat.id, questMas[que_num].image, caption=questMas[que_num].task, reply_markup=answer)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'ЕГЭ🇷🇺':
        bot.exam()
    elif message.text == 'Таблица лидеров🏆':
        bot.send_sticker(message.chat.id, stickers['ghoul'])


bot.polling()