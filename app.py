import telebot
from telebot import types
import smtplib
from email.message import EmailMessage

email = EmailMessage()

email ['from'] = "Siberia Tech"

email ['subject'] = """Сообщение от бота Siberia Tech"""

email.set_content("Вы расчитали доход от вклада в телеграм боте Siberia Tech")





bot = telebot.TeleBot("1242999554:AAFtFrFDrv7oRFVWaMBS7lm2brxFJD8fnho")


def keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Сделать Вклад')
    markup.add(btn1)
    return markup


@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    ok = types.InlineKeyboardButton(text="Понятно, вперёд!", callback_data="ok")
    keyboard.add(ok)
    bot.send_message(message.chat.id, """Здравствуйте! Добро пожаловать в телеграм-бот Sibiria Tech.
Здесь вы можете рассчитать доход от вашего вклада""", reply_markup=keyboard)

time = 0
amount = 0
reinvesting = 0

add_dict = {
    't0.5': 0.24,
    't1': 0.3,
    't1.5': 0.36
}
time_dict = {
    't0.5': 'МИНИ',
    't1': 'СТАНДАРТ',
    't1.5': 'ОПТИМУМ'
}


checker = None
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "ok":
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            a = types.InlineKeyboardButton(text="🔰 Мини - 6 мес - 1 год. 24% годовых 🔰", callback_data="t0.5")

            b = types.InlineKeyboardButton(text="🔰 Стандарт - 1 - 1,5 года. 30% годовых 🔰", callback_data="t1")
            c = types.InlineKeyboardButton(text="🔰 Оптимум - более 1,5 лет. 36% годовых 🔰", callback_data="t1.5")


            keyboard.add(a,b,c)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Пожалуйста, выберите период""", reply_markup=keyboard)

        if call.data[0] == 't':
            time = call.data

            keyboard = types.InlineKeyboardMarkup(row_width=1)
            if time == 't0.5':
                keyboard.add(types.InlineKeyboardButton(text="125,000 р.", callback_data="a125_"+call.data))
                keyboard.add(types.InlineKeyboardButton(text="250,000 р.", callback_data="a250_"+call.data))
            if time != 't0.5':
                keyboard.add(types.InlineKeyboardButton(text="500,000 р.", callback_data="a500_"+call.data))
                keyboard.add(types.InlineKeyboardButton(text="1 млн р.", callback_data="a1000_"+call.data))
                keyboard.add(types.InlineKeyboardButton(text="10 млн р.", callback_data="a10000_"+call.data))
                keyboard.add(types.InlineKeyboardButton(text="50 млн р.", callback_data="a50000_"+call.data))
                keyboard.add(types.InlineKeyboardButton(text="100 млн р.", callback_data="a100000_"+call.data))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = f"""Вы выбрали период "{time_dict[time]}. {add_dict[time]*100}% годовых ✅"
Пожалуйста,выберите сумму""", reply_markup=keyboard)
            print(checker)
        if call.data[0] == 'a':
            amount = call.data

            keyboard = types.InlineKeyboardMarkup(row_width=1)

            keyboard.add(types.InlineKeyboardButton(text="0%", callback_data="r0_"+call.data))
            keyboard.add(types.InlineKeyboardButton(text="50%", callback_data="r50_"+call.data))
            keyboard.add(types.InlineKeyboardButton(text="100%", callback_data="r100_"+call.data))

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = f"""Вы выбрали сумму {amount[1:4]}000 р.
Пожалуйста,выберите реинвестиции""", reply_markup=keyboard)
        if call.data[0] == 'r':

            keyboard = types.InlineKeyboardMarkup()
            da = types.InlineKeyboardButton(text="Да, конечно!", callback_data="das")
            net = types.InlineKeyboardButton(text="Нет, спасибо", callback_data="nets")
            keyboard.add(da,net)


            reinvesting, amount, time = call.data.split('_')

            profit = int(float(time[1:]) * float(amount[1:]) * add_dict[time])
            coef = round(1+(add_dict[time] + 0.5) * float(reinvesting[1:])  / 100,4)
            if time == 't1.5':

                s = f"Ваш доход при периоде {time_dict[time]}, сумме вноса {amount[1:]}000 р. и ставке реинвестирования {reinvesting[1:]}% составит {profit}000 р. за полгода"
                if coef != 1.0:
                    s+= f" и будет увеличиваться каждый год в геометрической прогрессии с множителем {coef}"
                else:
                    s+= f", то есть {round(profit*1000/6,2)} р. в месяц"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = s)
                bot.send_message(call.message.chat.id, "Хотели бы вы сделать вклад?", reply_markup = keyboard)
            if time == 't0.5':
                s = f"Ваш доход при периоде {time_dict[time]}, сумме вноса {amount[1:]}000 р. и ставке реинвестирования {reinvesting[1:]}% составит {profit}000 р. за полгода и {profit*2}000 р. за год"
                if coef != 1.0:
                    s+= f" и будет увеличиваться каждый год в геометрической прогрессии с множителем {coef}"
                else:
                    s+= f", то есть {round(profit*1000/12,2)}р в месяц"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = s)
                bot.send_message(call.message.chat.id, "Хотели бы вы сделать вклад?", reply_markup = keyboard)
            if time == 't1':
                s = f" Ваш доход при периоде {time_dict[time]}, сумме вноса {amount[1:]}000 р. и ставке реинвестирования {reinvesting[1:]}% составит {profit}000 р. за год и {int(profit*1.5)}000 р. за полтора года"
                if coef != 1.0:
                    s+= f" и будет увеличиваться каждый год в геометрической прогрессии с множителем {coef}"
                else:
                    s+= f", то есть {round(profit*1000/12,2)} р. в месяц"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = s)
                bot.send_message(call.message.chat.id, "Хотели бы вы сделать вклад?", reply_markup = keyboard)


        if call.data == "das":
            bot.send_message(call.message.chat.id, 'Пожалуйста, укажите почту')
        if call.data == "nets":
            bot.send_message(call.message.chat.id, 'Спасибо, что пользуетесь нашими услугами!')




@bot.message_handler(content_types=['text'])
def send1_text(message):
    print(message.text)

    if "@" in message.text:
        email ['to'] = message.text
        with smtplib.SMTP(host = "smtp.gmail.com",port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("investsiberiatech@gmail.com", "12735334")
            smtp.send_message(email)
            print('Task Executed')
        bot.send_message(message.chat.id, 'СПАСИБО, НА ВАШ ПОЧТОВЫЙ ЯЩИК ПРИДЕТ СООБЩЕНИЕ С ДОКУМЕНТАМИ.') 

    else:
        bot.send_message(message.chat.id, 'Пожалуйста, укажите действительную почту')






bot.polling()
