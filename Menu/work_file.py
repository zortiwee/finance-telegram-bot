from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from FinanceData.data_finance import database_init
from menu_start import show_start_menu
from Menu.bot_instance import bot

#IMPORTANT COMMENTS
#this is the main file to run your bot because here you have bot.infinity_polling()



@bot.message_handler(commands=["start"])
def send_welcome(message):
    print("BOT ID = ", id(bot))

    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item_button1 = KeyboardButton(text="Yes")
    item_button2 = KeyboardButton(text="No")
    markup.add(item_button1)
    markup.add(item_button2)
    database_init()
    bot.send_message(message.chat.id, "Are you ready to track your finances?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Yes", "No"])
def start_buttons(message):
     if message.text == "Yes":
         show_start_menu(message)
     elif message.text == "No":
        bot.send_message(message.chat.id, "Thats not cool")



bot.infinity_polling()