from app.models.database import get_db_connection

class Transaction:
    @staticmethod
    def create(user_id, account_id, category_id, type, amount, tx_date, description=""):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO transactions 
               (user_id, account_id, category_id, type, amount, tx_date, description) 
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (user_id, account_id, category_id, type, amount, tx_date, description)
        )
        conn.commit()
        tx_id = cursor.lastrowid
        conn.close()
        return tx_id

    @staticmethod
    def get_all_by_user(user_id):
        conn = get_db_connection()
        query = """
            SELECT t.*, a.name as account_name, c.name as category_name
            FROM transactions t
            LEFT JOIN accounts a ON t.account_id = a.id
            LEFT JOIN categories c ON t.category_id = c.id
            WHERE t.user_id = ?
            ORDER BY t.tx_date DESC, t.id DESC
        """
        transactions = conn.execute(query, (user_id,)).fetchall()
        conn.close()
        return [dict(t) for t in transactions]

    @staticmethod
    def get_by_id(tx_id):
        conn = get_db_connection()
        tx = conn.execute("SELECT * FROM transactions WHERE id = ?", (tx_id,)).fetchone()
        conn.close()
        return dict(tx) if tx else None

    @staticmethod
    def delete(tx_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
        conn.commit()
        conn.close()
