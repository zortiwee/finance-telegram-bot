# 💰 Finance Tracker Bot

> **My first Python project** — a Telegram bot for personal finance tracking built with pyTelegramBotAPI and SQLite.

---

## 📖 About

Finance Tracker Bot is a Telegram bot that helps you manage personal finances directly from your phone. Create named money lists, track deposits and withdrawals, view your transaction history, and get monthly spending reports — all inside Telegram.

This is my **first independent Python project**, built without courses or mentors. It covers real-world concepts like multi-step conversation flows, persistent multi-user storage, modular project architecture, and transaction logging.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Create List** | Create a named finance list with a starting balance |
| 📋 **View Lists** | See all your lists with current balances |
| 💰 **Add Money** | Add funds to any existing list |
| 💸 **Take Money** | Subtract funds (with overdraft protection) |
| ✏️ **Rename List** | Change the name of any list |
| 🗑️ **Delete List** | Remove a list with a confirmation step |
| 📜 **Transaction History** | View your last 10 transactions with dates |
| 📊 **Monthly Report** | Full spending summary grouped by list for current month |
| 👥 **Multi-user** | Each user sees only their own data |
| 🔙 **Navigation** | Intuitive menu and sub-menu system with back button |

---

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **Bot Framework:** [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)
- **Database:** SQLite3 (built-in)
- **IDE:** PyCharm

---

## 📁 Project Structure

```
project/
├── Menu/
│   ├── bot_instance.py       # Bot initialization (single instance)
│   ├── menu_start.py         # Main menu, sub-menus & button handlers
│   ├── work_file.py          # Entry point, /start command
│   └── finance.db            # SQLite database (auto-created on first run)
└── FinanceData/
    ├── data_finance.py       # CRUD operations for finance lists
    ├── history.py            # Transaction history logic
    └── reports.py            # Monthly report generation
```

---

## 🗄️ Database Schema

```sql
-- Finance lists (one per user)
CREATE TABLE finance (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id  INTEGER NOT NULL,
    name     TEXT,
    numbers  INTEGER
);

-- Transaction log
CREATE TABLE history (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id       INTEGER NOT NULL,
    list_name     TEXT,
    operation     TEXT,
    amount        INTEGER,
    balance_after INTEGER,
    date          TEXT
);
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/zortiwee/finance-telegram-bot.git
   cd finance-telegram-bot
   ```

2. **Install dependencies**
   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Set your bot token as an environment variable**
   ```bash
   export BOT_TOKEN="your_token_here"
   ```

   In `bot_instance.py`:
   ```python
   import os
   TOKEN = os.getenv("BOT_TOKEN")
   ```

4. **Run the bot**
   ```bash
   python Menu/work_file.py
   ```

> The database file `finance.db` is created automatically on first run.

---

## 📱 How It Works

```
/start
  └── Are you ready? → Yes
        └── Main Menu
              ├── ➕ New List         → Enter name → Enter balance → Saved ✅
              ├── 📋 My Lists        → Shows all your lists with balances
              ├── ✏️ Rename List     → Pick ID → Enter new name → Updated ✅
              ├── 💰 Money
              │     ├── ➕ Add Money  → Pick ID → Enter amount → Updated ✅
              │     ├── ➖ Take Money → Pick ID → Enter amount → Updated ✅
              │     └── 🔙 Back
              ├── 🗑️ Delete List     → Pick ID → Confirm → Deleted ✅
              ├── 📜 History         → Last 10 transactions with dates
              └── 📊 Monthly Report  → Grouped summary for current month
```

---

## 📊 Monthly Report Example

```
📊 Monthly report — 06.2025
────────────────────────────

📋 Groceries
   ➕ Added:  8000Kč
   ➖ Taken:  5300Kč
   📈 Net:    2700Kč

📋 Rent
   ➕ Added:  15000Kč
   ➖ Taken:  15000Kč
   📈 Net:    0Kč

────────────────────────────
✅ Total added:  23000Kč
❌ Total taken:  20300Kč
📈 Net total:    2700Kč
```

---

## 🌱 What I Learned

- Structuring a multi-file Python project from scratch
- Working with `telebot` and multi-step conversation flows (`register_next_step_handler`)
- CRUD operations and schema design with SQLite3
- Fixing duplicate bot instances across modules (single import pattern)
- Passing arguments through conversation chains using lambda functions
- Per-user data isolation with `user_id` filtering
- Transaction logging and report generation
- Version control with Git and GitHub
- Debugging stack traces independently

---

## 🔮 Future Plans

- [ ] Deploy to a cloud server (Railway) for 24/7 uptime
- [ ] Migrate from SQLite to PostgreSQL for production
- [ ] Add per-category spending limits and alerts
- [ ] Export monthly report as PDF or CSV
- [ ] Support multiple currencies

---

## 👤 Author

**Andrew Borodavka**
- GitHub: [@zortiwee](https://github.com/zortiwee)

---

> *"Every expert was once a beginner."*
> This is where my journey started. 🚀
