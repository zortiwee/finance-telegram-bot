import sqlite3
from datetime import datetime
from Menu.bot_instance import bot

def history_init():
    data_base = sqlite3.connect('../Menu/finance.db')
    cursor = data_base.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        list_name TEXT,
        operation TEXT,
        amount INTEGER,
        balance_after INTEGER,
        date TEXT
        )""")

    data_base.commit()
    cursor.close()
    data_base.close()

def add_to_history(user_id, last_name, operation, amount, balance_after):
    data_base = sqlite3.connect('../Menu/finance.db')
    cursor = data_base.cursor()

    cursor.execute("""
        INSERT INTO history (user_id,list_name,operation,amount,balance_after,date)
        VALUES (?,?,?,?,?,?)
        """, (user_id, last_name, operation, amount, balance_after, datetime.now().strftime("%d.%m.%Y %H:%M")))

    data_base.commit()
    cursor.close()
    data_base.close()

def show_history(message):
    data_base = sqlite3.connect('../Menu/finance.db')
    cursor = data_base.cursor()

    cursor.execute("""
    SELECT list_name, operation, amount, balance_after, date
    FROM history WHERE user_id = ? ORDER BY id DESC LIMIT 10
    """, (message.from_user.id,))

    rows = cursor.fetchall()
    cursor.close()
    data_base.close()

    if not rows:
        bot.send_message(message.chat.id, "No transaction history yet")
        return

    text = "📜 Last 10 transactions:\n\n"
    for row in rows:
        list_name, operation, amount, balance_after, date = row
        emoji = "➕" if operation == "add" else "➖"
        text += (
            f"{emoji} {list_name}\n"
            f"   Amount: {amount}Kč | Balance after: {balance_after}Kč\n"
            f"   📅 {date}\n\n"
        )

    bot.send_message(message.chat.id, text)
