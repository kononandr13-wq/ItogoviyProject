import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login VARCHAR(1000) NOT NULL,
            password VARCHAR(1000) NOT NULL
        )
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text VARCHAR(1000) NOT NULL,
            is_done BOOLEAN DEFAULT FALSE,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")  # Исправлено: User вместо users
    users = cursor.fetchall()
    conn.close()
    return users

def auth_user(login, password):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM user WHERE login=?", (login,)
    )
    user = cursor.fetchone()
    if not user:
        return None
    
    if check_password_hash(user[2], password):
        return {
            "user_id": user[0],
            "user_login": user[1]
        }
    else:
        return -1

def add_user(login, password):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO User (login, password) VALUES (?,?)",
        (login, hashed_password)
    )
    print("Создан пользователь " + login)
    conn.commit()
    conn.close()

def is_user_exists(login):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE login = ?", (login,))
    user = cursor.fetchone()
    conn.close()  # Добавлено закрытие соединения
    return user is not None

if __name__ == "__main__":
    create_db()
    add_user("21", "21")
    add_user("user", "user")
    users = get_users()





