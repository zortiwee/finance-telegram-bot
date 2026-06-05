from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from FinanceData.data_finance import get_list_name_start, callback, get_list_to_edit, get_list_to_add_money, get_list_to_take_money,get_list_to_delete
from FinanceData.history import show_history
from FinanceData.reports import show_monthly_report
from Menu.bot_instance import bot


def show_start_menu(message):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    markup.add(
        KeyboardButton("➕ New List"),
        KeyboardButton("📋 My Lists"),
        KeyboardButton("✏️ Rename List"),
        KeyboardButton("💰 Money"),
        KeyboardButton("🗑️ Delete List"),
        KeyboardButton("📜 History"),
        KeyboardButton("📊 Monthly Report")
    )

    bot.send_message(message.chat.id, "What are we going to work with?", reply_markup=markup)


def show_money_menu(message):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    markup.add(
        KeyboardButton("➕ Add Money"),
        KeyboardButton("➖ Take Money"),
        KeyboardButton("🔙 Back")
    )

    bot.send_message(message.chat.id, "Choose an action:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in [
    "➕ New List", "📋 My Lists", "✏️ Rename List", "💰 Money",
    "➕ Add Money", "➖ Take Money", "🔙 Back","🗑️ Delete List",
    "📜 History", "📊 Monthly Report"
])
def handle_buttons(message):
    if message.text == "➕ New List":
        get_list_name_start(message)
    elif message.text == "📋 My Lists":
        callback(message)
    elif message.text == "✏️ Rename List":
        get_list_to_edit(message)
    elif message.text == "💰 Money":
        show_money_menu(message)   # ← переходим в сабменю
    elif message.text == "➕ Add Money":
        get_list_to_add_money(message)
    elif message.text == "➖ Take Money":
        get_list_to_take_money(message)
    elif message.text == "🔙 Back":
        show_start_menu(message)
    elif message.text == "🗑️ Delete List":
        get_list_to_delete(message)
    elif message.text == "📜 History":
        show_history(message)
    elif message.text == "📊 Monthly Report":
        show_monthly_report(message)
