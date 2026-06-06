from Menu.bot_instance import bot
from FinanceData.FinanceDB import FinanceDB

db = FinanceDB('../Menu/finance.db')

def show_history(message):

    rows = db.get_history(message.from_user.id)

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
