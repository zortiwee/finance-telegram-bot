import sqlite3
from datetime import datetime

# class for data base

class FinanceDB:
    def __init__(self, db_path):
        self.db_path = db_path

#------------DATA-FINANCE file---------------

    def get_lists(self, user_id):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute('SELECT * FROM finance WHERE user_id = ?', (user_id,))
        result = cursor.fetchall()
        cursor.close()
        data_base.close()
        return result

    def save_list(self, user_id, name, balance):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute(
            "INSERT INTO finance (user_id, name, numbers) VALUES (?, ?, ?)",
            (user_id, name, balance)
        )
        data_base.commit()
        cursor.close()
        data_base.close()

    def get_list_by_id(self, user_id, list_id):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()

        cursor.execute('SELECT * FROM finance WHERE id = ? AND user_id = ?', (list_id, user_id))

        found = cursor.fetchone()
        cursor.close()
        data_base.close()
        return found

    def update_list(self, user_id, list_id, name=None, balance=None):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()

        if name is not None:
            cursor.execute(
                "UPDATE finance SET name = ? WHERE id = ? AND user_id = ?",
                (name, list_id, user_id)
            )

        if balance is not None:
            cursor.execute(
                "UPDATE finance SET numbers = ? WHERE id = ? AND user_id = ?",
                (balance, list_id, user_id)
            )

        data_base.commit()
        cursor.close()
        data_base.close()

    def delete_list(self, user_id, list_id):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute("DELETE FROM finance WHERE id = ? AND user_id = ?", (list_id, user_id))
        data_base.commit()
        cursor.close()
        data_base.close()

        # --- HISTORY ---
    def history_initialization(self):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            list_name TEXT,
            operation TEXT,
            amount INTEGER,
            balance_after INTETEGR,
            balance_after INTEGER,
            date TEXT
            )""")

        data_base.commit()
        cursor.close()
        data_base.close()

    def add_to_history(self, user_id, list_name, operation, amount, balance_after):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute("""
            INSERT INTO history (user_id, list_name, operation, amount, balance_after, date)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, list_name, operation, amount, balance_after, datetime.now().strftime("%d.%m.%Y %H:%M")))

        data_base.commit()
        cursor.close()
        data_base.close()

    def get_history(self, user_id):
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute("""
             SELECT list_name, operation, amount, balance_after, date
             FROM history
             WHERE user_id = ?
             ORDER BY id DESC LIMIT 10
             """, (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        data_base.close()
        return rows

        # --- REPORTS ---
    def get_monthly_data(self, user_id):
        current_month = datetime.now().strftime("%m.%Y")
        data_base = sqlite3.connect(self.db_path)
        cursor = data_base.cursor()
        cursor.execute("""
            SELECT list_name, operation, amount
            FROM history
            WHERE user_id = ? AND date LIKE ?
            """, (user_id, f"%.{current_month}%"))
        rows = cursor.fetchall()
        cursor.close()
        data_base.close()
        return rows