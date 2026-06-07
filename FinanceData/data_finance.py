import sqlite3
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from Menu.bot_instance import bot
from FinanceData.FinanceDB import FinanceDB

# IMPORTANT COMMENTS
# this file has all the functions for all the buttons and your sqlite dataBase
# it can be a little bit messy but you can understand role of the function by it name
# dataBase file will appear automatically after bots first run

db = FinanceDB('../Menu/finance.db')
MAX_BALANCE = 10_000_000

def database_init():
    data_base = sqlite3.connect('../Menu/finance.db')
    cursor = data_base.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS finance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT,
    numbers INTEGER
    )""")

    data_base.commit()
    cursor.close()
    data_base.close()

    db.history_initialization()

def get_list_name_start(message):
    msg = bot.send_message(message.chat.id,"Enter name of new list")
    bot.register_next_step_handler(msg, get_list_name)


def get_list_name(message):
    print("GET_LIST_NAME_CALLLED")
    name = message.text

    bot.send_message(message.chat.id, "Enter amount of money")

    bot.register_next_step_handler(message, lambda msg: save_list(msg, name))


def save_list(message, name):
    if len(name) > 50:
        bot.send_message(message.chat.id, "❌ Name too long, max 50 characters")
        return

    try:
        balance = int(message.text)  # ← один раз

        if balance < 0 or balance > MAX_BALANCE:
            bot.send_message(message.chat.id, "❌ Invalid amount, max 10 000 000")
            return

        user_id = message.from_user.id
        db.save_list(user_id, name, balance)
        bot.send_message(message.chat.id, f"✅ List {name} created with balance {balance} Kč")

    except ValueError:
        bot.send_message(message.chat.id, "‼️Please enter a valid number")

def callback(message):

    lists = db.get_lists(message.from_user.id)

    if not lists:
        bot.send_message(message.chat.id, "No lists found")
        return

    info = "Your lists:\n"
    for element in lists:
        info += f"ID: {element[0]} | Name: {element[2]} | Balance: {element[3]}Kč\n"

    bot.send_message(message.chat.id, info)

def get_list_to_edit(message):
    all_lists = db.get_lists(message.from_user.id)

    if not all_lists:
        bot.send_message(message.chat.id,"No lists found")
        return

    info = "Your lists:\n"
    for element in all_lists:
        info += f"ID: {element[0]}, Name: {element[2]}, Amount: {element[3]}\n"

    msg = bot.send_message(message.chat.id, info + "\n‼️Enter ID of the list that you want to edit")
    bot.register_next_step_handler(msg, get_new_name)

def get_new_name(message):
    try:
        list_id = int(message.text)

        found = db.get_list_by_id(message.from_user.id, list_id)

        if not found:
            bot.send_message(message.chat.id,"List with this ID doesn't exist")
            return

        msg = bot.send_message(message.chat.id, f"Name: {found[2]}, Enter new name:")
        bot.register_next_step_handler(msg,lambda m: save_edited_name(m, list_id))

    except ValueError:
        bot.send_message(message.chat.id,"‼️Please enter a valid number")

def save_edited_name(message, list_id):
    new_name = message.text
    db.update_list(message.from_user.id, list_id, name=new_name)
    bot.send_message(message.chat.id, "✅ Name updated!")


def get_list_to_add_money(message):

    all_lists = db.get_lists(message.from_user.id)

    if not all_lists:
        bot.send_message(message.chat.id, "No lists found")
        return

    info = "Your lists:\n"
    for element in all_lists:
        info += f"ID: {element[0]} | Name: {element[2]} | Balance: {element[3]}Kč\n"

    msg = bot.send_message(message.chat.id, info + "‼\n‼️Enter ID of the list:")
    bot.register_next_step_handler(msg, lambda m: get_amount_to_change(m, "add"))


def get_list_to_take_money(message):

    all_lists = db.get_lists(message.from_user.id)

    if not all_lists:
        bot.send_message(message.chat.id, "No lists found")
        return

    info = "Your lists:\n"
    for element in all_lists:
        info += f"ID: {element[0]} | Name: {element[2]} | Balance: {element[3]}Kč\n"

    msg = bot.send_message(message.chat.id, info + "️\n‼️Enter ID of the list:")
    # ✅ operation передаётся сразу здесь
    bot.register_next_step_handler(msg, lambda m: get_amount_to_change(m, "take"))


def get_amount_to_change(message, operation):
    try:
        list_id = int(message.text)

        found = db.get_list_by_id(message.from_user.id, list_id)

        if not found:
            bot.send_message(message.chat.id, "‼️List with this ID not found")
            return

        action = "add to" if operation == "add" else "take from"
        msg = bot.send_message(
            message.chat.id,
            f"Current balance: {found[3]}Kč\nHow much to {action} the list?"
        )
        # ✅ и list_id и operation передаются через lambda
        bot.register_next_step_handler(msg, lambda m: update_balance(m, list_id, operation))

    except ValueError:
        bot.send_message(message.chat.id, "‼️Please enter a valid ID (number)")


def update_balance(message, list_id, operation):
    try:
        amount = int(message.text)
        found = db.get_list_by_id(message.from_user.id, list_id)
        current = found[3]

        if operation == "add":
            new_balance = current + amount
        else:
            if amount > current:
                bot.send_message(message.chat.id, f"❌ Not enough money! Current: {current}Kč")
                return
            new_balance = current - amount

        db.update_list(message.from_user.id, list_id, balance=new_balance)
        emoji = "➕" if operation == "add" else "➖"
        bot.send_message(message.chat.id, f"{emoji} Done! New balance: {new_balance}Kč")

    except ValueError:
        bot.send_message(message.chat.id, "‼️Please enter a valid number")


def get_list_to_delete(message):

    all_lists = db.get_lists(message.from_user.id)

    if not all_lists:
        bot.send_message(message.chat.id, "No lists found")
        return

    info = "Your lists:\n"
    for element in all_lists:
        info += f"ID: {element[0]} | Name: {element[2]} | Balance: {element[3]}Kč\n"

    msg = bot.send_message(message.chat.id, info + "\n‼️Enter ID of the list to delete‼:")
    bot.register_next_step_handler(msg, confirm_delete)


def confirm_delete(message):
    try:
        list_id = int(message.text)

        found = db.get_list_by_id(message.from_user.id, list_id)

        if not found:
            bot.send_message(message.chat.id, "List with this ID not found")
            return

        # Просим подтверждение перед удалением
        markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add(
            KeyboardButton("✅ Yes, delete"),
            KeyboardButton("❌ Cancel")
        )

        msg = bot.send_message(
            message.chat.id,
            f"Are you sure you want to delete:\n📋 {found[2]} | {found[3]}Kč?",
            reply_markup=markup
        )
        bot.register_next_step_handler(msg, lambda m: delete_list(m, list_id))

    except ValueError:
        bot.send_message(message.chat.id, "‼️Please enter a valid ID (number)")


def delete_list(message, list_id):
    if message.text == "✅ Yes, delete":

        db.delete_list(message.from_user.id, list_id)

        bot.send_message(message.chat.id, "🗑️ List deleted!")

    elif message.text == "❌ Cancel":
        bot.send_message(message.chat.id, "Cancelled.")

    from Menu.menu_start import show_start_menu
    show_start_menu(message)