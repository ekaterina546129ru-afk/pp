import sqlite3

DB_NAME = "home_routine.db"


def init_db() -> None:
    """Create tasks table if it does not exist."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                category TEXT NOT NULL,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                is_done INTEGER DEFAULT 0
            );
            """
        )
        conn.commit()


def add_task(user_id: int, category: str, title: str, date: str) -> None:
    """Add a new user task."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO tasks (user_id, category, title, date) VALUES (?, ?, ?, ?)",
            (user_id, category, title, date),
        )
        conn.commit()


def get_tasks(user_id: int, only_not_done: bool = False) -> list[tuple]:
    """Get user tasks, optionally only unfinished."""
    query = "SELECT id, category, title, date, is_done FROM tasks WHERE user_id = ?"
    params: tuple = (user_id,)

    if only_not_done:
        query += " AND is_done = 0"

    query += " ORDER BY id"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(query, params)
        return cursor.fetchall()


def mark_task_done(user_id: int, task_id: int) -> bool:
    """Mark task as done. Return True if task exists."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "UPDATE tasks SET is_done = 1 WHERE user_id = ? AND id = ?",
            (user_id, task_id),
        )
        conn.commit()
        return cursor.rowcount > 0


def delete_task(user_id: int, task_id: int) -> bool:
    """Delete task. Return True if task exists."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE user_id = ? AND id = ?",
            (user_id, task_id),
        )
        conn.commit()
        return cursor.rowcount > 0
