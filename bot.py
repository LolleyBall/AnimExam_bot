import telebot
from telebot import types
import config
from questions import questMas
from questions import answerPack
from questions import wrongAnswers
import random
from stickers import stickers

bot = telebot.TeleBot(config.token)
que_num = ''
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
button1 = types.KeyboardButton('ЕГЭ🇷🇺')
button2 = types.KeyboardButton('Таблица лидеров🏆')
button3 = types.KeyboardButton('Оставить отзыв')
keyboard1.add(button1, button2, button3)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, вы попали на ЕГЭ по аниме, что будете делать?', reply_markup=keyboard1 )


def exam(message):
    global que_num
    answer = types.InlineKeyboardMarkup()
    que_num = int(random.uniform(0, len(questMas)))
    is_correct = False
    for i in range(4):
        index = int(random.uniform(0, len(answerPack)))
        if i == 3 and is_correct == False:
            index = questMas[que_num].answer
        if index == questMas[que_num].answer:
            is_correct = True
        answer.add(types.InlineKeyboardButton(answerPack[index], callback_data=str(index)))
    bot.send_photo(message.chat.id, questMas[que_num].image, caption=questMas[que_num].task, reply_markup=answer)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'ЕГЭ🇷🇺':
        exam(message)
    elif message.text == 'Таблица лидеров🏆':
        bot.send_sticker(message.chat.id, stickers['ghoul'])


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == str(questMas[que_num].answer):
                bot.send_message(call.message.chat.id, 'Это же ' + answerPack[questMas[que_num].answer] + '! Правильно!!!')
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
            else:
                bot.send_message(call.message.chat.id, 'Это не ' + answerPack[int(call.data)] + '. ' + wrongAnswers[int(random.uniform(0, len(wrongAnswers)))])
                bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ответ принят")
    except Exception as e:
        print(repr(e))
    # finally:
    #     correct = types.InlineKeyboardMarkup()
    #     correct.add(types.InlineKeyboardButton(, callback_data=None))
    #     bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=correct)

bot.polling()