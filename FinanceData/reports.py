from datetime import datetime
from Menu.bot_instance import bot
from FinanceData.FinanceDB import FinanceDB

db = FinanceDB('../Menu/finance.db')

def show_monthly_report(message):

    rows = db.get_monthly_data(message.from_user.id)
    current_month = datetime.today().strftime("%m.%Y")

    if not rows:
        bot.send_message(message.chat.id, f"NO transaction in {current_month}")
        return

    total_added = sum(r[2] for r in rows if r[2] == "add")
    total_taken = sum(r[2] for r in rows if r[1] == "take")

    by_list = {}
    for list_name, operation, amount in rows:
        if list_name not in by_list:
            by_list[list_name] = {"added": 0, "taken": 0}
        if operation == "add":
            by_list[list_name]["added"] += amount
        else:
            by_list[list_name]["taken"] += amount

    text = f"📊 Monthly report — {current_month}\n"
    text += "─" * 28 + "\n\n"

    for list_name, data in by_list.items():
        text += f"📋 {list_name}\n"
        text += f"   ➕ Added:  {data['added']}Kč\n"
        text += f"   ➖ Taken:  {data['taken']}Kč\n"
        text += f"   📈 Net:    {data['added'] - data['taken']}Kč\n\n"

    text += "─" * 28 + "\n"
    text += f"✅ Total added:  {total_added}Kč\n"
    text += f"❌ Total taken:  {total_taken}Kč\n"
    text += f"📈 Net total:    {total_added - total_taken}Kč"

    bot.send_message(message.chat.id, text)
