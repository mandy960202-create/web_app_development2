from app.models.database import get_db_connection

class Account:
    @staticmethod
    def create(user_id, name, type, balance=0):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO accounts (user_id, name, type, balance) VALUES (?, ?, ?, ?)",
            (user_id, name, type, balance)
        )
        conn.commit()
        account_id = cursor.lastrowid
        conn.close()
        return account_id

    @staticmethod
    def get_all_by_user(user_id):
        conn = get_db_connection()
        accounts = conn.execute("SELECT * FROM accounts WHERE user_id = ?", (user_id,)).fetchall()
        conn.close()
        return [dict(a) for a in accounts]

    @staticmethod
    def get_by_id(account_id):
        conn = get_db_connection()
        account = conn.execute("SELECT * FROM accounts WHERE id = ?", (account_id,)).fetchone()
        conn.close()
        return dict(account) if account else None

    @staticmethod
    def update_balance(account_id, new_balance):
        conn = get_db_connection()
        conn.execute("UPDATE accounts SET balance = ? WHERE id = ?", (new_balance, account_id))
        conn.commit()
        conn.close()
