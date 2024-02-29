@bot.message_handler(comands=['cars'])
def cars(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Марки ТС')
    btn2 = types.KeyboardButton('Объем')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Привет'.format(message.from_user), reply_markup=markup)


