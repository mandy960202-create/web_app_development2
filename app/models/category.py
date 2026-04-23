from app.models.database import get_db_connection

class Category:
    @staticmethod
    def create(user_id, name, type, budget=0):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO categories (user_id, name, type, budget) VALUES (?, ?, ?, ?)",
            (user_id, name, type, budget)
        )
        conn.commit()
        category_id = cursor.lastrowid
        conn.close()
        return category_id

    @staticmethod
    def get_all_by_user(user_id):
        conn = get_db_connection()
        categories = conn.execute("SELECT * FROM categories WHERE user_id = ?", (user_id,)).fetchall()
        conn.close()
        return [dict(c) for c in categories]

    @staticmethod
    def get_by_id(category_id):
        conn = get_db_connection()
        category = conn.execute("SELECT * FROM categories WHERE id = ?", (category_id,)).fetchone()
        conn.close()
        return dict(category) if category else None
