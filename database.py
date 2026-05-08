import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
<<<<<<< HEAD
            level VARCHAR(1000) NOT NULL,
            level VARCHAR(1000) NOT NULL
=======
            login VARCHAR(1000) NOT NULL,
            password VARCHAR(1000) NOT NULL
>>>>>>> parent of 57a5d54 (database)
        )
    '''
    cursor.execute(sql)

    # Добавление 3 уровней доступа (Первый, Второй, Третий)
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Первый уровень')")
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Второй уровень')")
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Третий уровень')")

    sql = '''
<<<<<<< HEAD
        CREATE TABLE IF NOT EXISTS gos_persona (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
@ -27,7 +32,7 @@ def create_db():
=======
        CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text VARCHAR(1000) NOT NULL,
            is_done BOOLEAN DEFAULT FALSE,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User(id)
>>>>>>> parent of 57a5d54 (database)
        )
    '''
    cursor.execute(sql)
    conn.commit()
<<<<<<< HEAD
    

    sql = '''
        CREATE TABLE IF NOT EXISTS file (
            def create_db():
            reason VARCHAR(1000) NOT NULL,
            notes VARCHAR(1000) NOT NULL,
            photo VARCHAR(1000) NOT NULL,
            tickets VARCHAR(1000) NOT NULL,
            tickets VARCHAR(1000) NOT NULL
        )
    '''
    cursor.execute(sql)
def create_db():
    
    cursor.execute(sql)


    conn.commit()

=======
>>>>>>> parent of 57a5d54 (database)
    conn.close()

def get_users():
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    cursor.execute("SELECT * FROM Dostyp")
    users = cursor.fetchall()
    conn.close()
    return users

def auth_user(login, password):
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()

    cursor.execute(
        def auth_user(login, password):
    else:
        return -1

def add_user(login, password):
    conn = sqlite3.connect("todo.db")
def add_citizens(name,surname, patronymic,is_wanted):
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)

    cursor.execute(
        "INSERT INTO file(reason,notes,photo,tickets)VALUES(?,?,?,?)",
        ('', '','','')
    )

    new_file_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO User (login, password) VALUES (?,?)",
        (login, hashed_password)
        "INSERT INTO Citizens (name,surname, patronymic,is_wanted,file_id) VALUES (?,?,?,?,?)",
        (name,surname, patronymic,is_wanted, new_file_id)
    )
    print("Создан пользователь " + login)
    print("Создан пользователь " + name,surname,patronymic)
    conn.commit()
    conn.close()

def is_user_exists(login):
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE login = ?", (login,))
    user = cursor.fetchone()
def is_user_exists(login):

if __name__ == "__main__":
    create_db()
    add_user("21", "21")
    add_user("user", "user")
    users = get_users()
    add_citizens("tIMUR", "sHUPOAWLDKAWLJKD", "HZ", 1)
users = get_users()









