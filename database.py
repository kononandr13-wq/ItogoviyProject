import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS Dostyp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level VARCHAR(1000) NOT NULL,
        )
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE IF NOT EXISTS gos_persona (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            rank VARCHAR(1000) NOT NULL,
            Name VARCHAR(1000) NOT NULL,
            Surname VARCHAR(1000) NOT NULL,
            Patronymic VARCHAR(1000) NOT NULL,
            login VARCHAR(1000) NOT NULL,
            password VARCHAR(1000) NOT NULL,
            dostyp_id INTEGER NOT NULL,
            FOREIGN KEY (dostyp_id) REFERENCES Dostyp(id)
        )
    '''

    cursor.execute(sql)
    conn.commit()
    
    sql = '''
        CREATE TABLE IF NOT EXISTS file (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reason VARCHAR(1000) NOT NULL,
            notes VARCHAR(1000) NOT NULL,
            photo VARCHAR(1000) NOT NULL,
            tickets VARCHAR(1000) NOT NULL,
        )
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE IF NOT EXISTS Citizens (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(1000) NOT NULL,
            Surname VARCHAR(1000) NOT NULL,
            Patronymic VARCHAR(1000) NOT NULL,
            is_wanted INTEGER DEFAULT NULL,
            file_id INTEGER NOT NULL,
            FOREIGN KEY (file_id) REFERENCES file(id)
        )
    '''
    cursor.execute(sql)



    conn.close()

def get_users():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
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
    conn.close()
    return user is not None

if __name__ == "__main__":
    create_db()
    add_user("21", "21")
    add_user("user", "user")
    users = get_users()





