import sqlite3

class FinanceDB:
    def __init__(self, db_path):
        self.db_path = db_path

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