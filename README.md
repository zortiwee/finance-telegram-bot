# 💰 Finance Tracker Bot

> **My first Python project** — a Telegram bot for personal finance tracking built with pyTelegramBotAPI and SQLite.

---

## 📖 About

Finance Tracker Bot is a simple yet functional Telegram bot that helps you keep track of your personal finances. You can create named money lists, add or subtract funds, rename them, and delete them — all from within Telegram.

This project was built as my **first hands-on experience** with Python, bot development, and working with databases. It covers real-world concepts like multi-step conversation flows, persistent storage, and modular project structure.

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
│   ├── bot_instance.py      # Bot initialization
│   ├── menu_start.py        # Main menu & button handlers
│   ├── work_file.py         # Entry point, /start command
│   └── finance.db           # SQLite database
└── FinanceData/
    └── data_finance.py      # All database logic & bot handlers
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

3. **Set your bot token**

   Create a `.env` file or set an environment variable:
   ```bash
   export BOT_TOKEN="your_token_here"
   ```

   Then in `bot_instance.py`:
   ```python
   import os
   TOKEN = os.getenv("BOT_TOKEN")
   ```

4. **Run the bot**
   ```bash
   python Menu/work_file.py
   ```

---

## 📱 How It Works

```
/start
  └── Are you ready? → Yes
        └── Main Menu
              ├── ➕ New List       → Enter name → Enter balance → Saved ✅
              ├── 📋 My Lists      → Shows all lists with balances
              ├── ✏️ Rename List   → Pick ID → Enter new name → Updated ✅
              ├── 💰 Money
              │     ├── ➕ Add Money  → Pick ID → Enter amount → Updated ✅
              │     ├── ➖ Take Money → Pick ID → Enter amount → Updated ✅
              │     └── 🔙 Back
              └── 🗑️ Delete List   → Pick ID → Confirm → Deleted ✅
```

---

## 🌱 What I Learned

- Structuring a multi-file Python project
- Working with the `telebot` library and multi-step conversation flows (`register_next_step_handler`)
- CRUD operations with SQLite3
- Avoiding common bugs like duplicate bot instances across modules
- Using lambda functions to pass arguments through conversation chains
- Version control with Git and GitHub

---

## 🔮 Future Plans

- [ ] Add per-user data (currently all users share the same database)
- [ ] Add transaction history / spending log
- [ ] Monthly summary reports
- [ ] Currency selection support
- [ ] Deploy to a cloud server (e.g. Railway, VPS)

---

## 👤 Author

**Andrew Borodavka**
- GitHub: [@zortiwee](https://github.com/zortiwee)

---

> *"Every expert was once a beginner."*
> This is where my journey started. 🚀
