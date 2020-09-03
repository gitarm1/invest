import telebot
from telebot import types

bot = telebot.TeleBot("1078971033:AAF8-JFPzo3wirwyKPPjeWcYCdzy8T-ylvI")


@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    ok = types.InlineKeyboardButton(text="Понял, вперёд!", callback_data="ok")
    keyboard.add(ok)
    bot.send_message(message.chat.id, """Здравствуйте! Добро пожаловать в телеграм-бот Sibiria Tech.
Здесь вы можете рассчитать доход от ваших инвестиций""", reply_markup=keyboard)


checker = None
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "ok":
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            a = types.InlineKeyboardButton(text="🔰 Мини - 6 мес - 1 год. 24% годовых 🔰", callback_data="mini")

            b = types.InlineKeyboardButton(text="🔰 Стандарт - 1 - 1,5 года. 30% годовых 🔰", callback_data="standart")
            c = types.InlineKeyboardButton(text="🔰 Оптимум - более 1,5 лет. 36% годовых 🔰", callback_data="optimus")


            keyboard.add(a,b,c)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Пожалуйста, выберите период""", reply_markup=keyboard)


        if call.data == "mini":
            f = open("text.txt","w+")
            f.write("mini")
            f.close()

            keyboard = types.InlineKeyboardMarkup(row_width=1)

            d = types.InlineKeyboardButton(text="125,000 р.", callback_data="125")
            l = types.InlineKeyboardButton(text="250,000 р.", callback_data="250")
            e = types.InlineKeyboardButton(text="500,000 р.", callback_data="500")
            f = types.InlineKeyboardButton(text="1 млн р.", callback_data="mln")
            g = types.InlineKeyboardButton(text="10 млн р.", callback_data="10mln")
            h = types.InlineKeyboardButton(text="50 млн р.", callback_data="50mln")
            j = types.InlineKeyboardButton(text="100 млн р.", callback_data="100mln")

            keyboard.add(d,l)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Вы выбрали период "Мини - 6 мес - 1 год. 24% годовых ✅"
Пожалуйста,выберите сумму""", reply_markup=keyboard)
            print(checker)
        if call.data == "standart":
            f = open("text.txt","w+")
            f.write("standart")
            f.close()
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            d = types.InlineKeyboardButton(text="125,000 р.", callback_data="125")
            l = types.InlineKeyboardButton(text="250,000 р.", callback_data="250")
            e = types.InlineKeyboardButton(text="500,000 р.", callback_data="500")
            f = types.InlineKeyboardButton(text="1 млн р.", callback_data="mln")
            g = types.InlineKeyboardButton(text="10 млн р.", callback_data="10mln")
            h = types.InlineKeyboardButton(text="50 млн р.", callback_data="50mln")
            j = types.InlineKeyboardButton(text="100 млн р.", callback_data="100mln")

            keyboard.add(l,e,f,g,h,j)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Вы выбрали период "Стандарт - 1 - 1,5 года. 30% годовых ✅"
Пожалуйста,выберите сумму""", reply_markup=keyboard)
            print("standart")

        if call.data == "optimus":
            f = open("text.txt","w+")
            f.write("optimus")
            f.close()
            keyboard = types.InlineKeyboardMarkup(row_width=1)

            d = types.InlineKeyboardButton(text="125,000 р.", callback_data="125")
            l = types.InlineKeyboardButton(text="250,000 р.", callback_data="250")
            e = types.InlineKeyboardButton(text="500,000 р.", callback_data="500")
            f = types.InlineKeyboardButton(text="1 млн р.", callback_data="mln")
            g = types.InlineKeyboardButton(text="10 млн р.", callback_data="10mln")
            h = types.InlineKeyboardButton(text="50 млн р.", callback_data="50mln")
            j = types.InlineKeyboardButton(text="100 млн р.", callback_data="100mln")

            keyboard.add(l,e,f,g,h,j)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,  text = """Вы выбрали период "Оптимум - более 1,5 лет. 36% годовых ✅"
Пожалуйста,выберите сумму""", reply_markup=keyboard)
            print("optimus")



        f = open("text.txt","r+")
        readed = f.read()

        if call.data == "125" and readed == "mini":

            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
    Пол года - 15,000 рублей💸
    Год - 30,000 рублей (2500р. в месяц)💸""")


        if call.data == "250" and readed == "mini":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Пол года - 30,000 рублей💸
Год - 60,000 рублей (5000р. в месяц)💸""")

        if call.data == "250" and readed == "standart":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Год - 75,000 рублей💸
1.5 года - 112,500 рублей (6,250р. в месяц)💸""")

        if call.data == "250" and readed == "optimus":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
1.5 года - 125,000 рублей💸
♾ -  +7,500р. каждый месяц💸""")

        if call.data == "500" and readed == "mini":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Пол года - 60,000 рублей💸
Год - 120,000 рублей (10,000р. в месяц)💸""")

        if call.data == "500" and readed == "standart":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Год - 150,000 рублей💸
1.5 года - 225,000 рублей (12,500р. в месяц)💸""")

        if call.data == "500" and readed == "optimus":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
1.5 года - 270,000 рублей💸
♾ -  +15,000р. каждый месяц💸""")


        if call.data == "mln" and readed == "mini":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Пол года - 120,000 рублей💸
Год - 240,000 рублей (20,000р. в месяц)💸""")


        if call.data == "mln" and readed == "standart":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Год - 300,000 рублей💸
1.5 года - 500,000 рублей (25,000р. в месяц)💸""")


        if call.data == "mln" and readed == "optimus":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
1.5 года - 540,000 рублей💸
♾ -  +30,000р. каждый месяц💸""")

        if call.data == "10mln" and readed == "mini":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Пол года - 1,200,000 рублей💸
Год - 2,400,000 рублей (200,000р. в месяц)💸""")


        if call.data == "10mln" and readed == "standart":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Год - 3,000,000 рублей💸
1.5 года - 5,000,000 рублей (250,000р. в месяц)💸""")


        if call.data == "10mln" and readed == "optimus":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
1.5 года - 5,400,000 рублей💸
♾ -  +300,000р. каждый месяц💸""")


        if call.data == "50mln" and readed == "mini":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Пол года - 6,000,000 рублей💸
Год - 12,000,000 рублей (1,000,000р. в месяц)💸""")


        if call.data == "50mln" and readed == "standart":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Год - 15,000,000 рублей💸
1.5 года - 25,000,000 рублей (1,250,000р. в месяц)💸""")


        if call.data == "50mln" and readed == "optimus":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
1.5 года - 27,000,000 рублей💸
♾ -  +1,500,000р. каждый месяц💸""")


        if call.data == "100mln" and readed == "mini":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Пол года - 12,000,000 рублей💸
Год - 24,000,000 рублей (2,000,000р. в месяц)💸""")

        if call.data == "100mln" and readed == "standart":
            bot.send_message(call.message.chat.id, """Ваш доход будет составлять:
Год - 30,000,000 рублей💸
1.5 года - 50,000,000 рублей (2,500,000р. в месяц)💸""")

bot.polling()
