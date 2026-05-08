import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("todo.db")
    conn = sqlite3.connect("fcb.db")
    cursor = conn.cursor()

    sql = '''
        CREATE TABLE IF NOT EXISTS Dostyp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            level VARCHAR(1000) NOT NULL,
            level VARCHAR(1000) NOT NULL
        )
    '''
    cursor.execute(sql)

    # Добавление 3 уровней доступа (Первый, Второй, Третий)
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Первый уровень')")
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Второй уровень')")
    cursor.execute("INSERT INTO Dostyp(level) VALUES('Третий уровень')")

    sql = '''
        CREATE TABLE IF NOT EXISTS gos_persona (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            tickets VARCHAR(1000) NOT NULL
            tickets VARCHAR(1000) NOT NULL,
        )
    '''
    cursor.execute(sql)
    conn.commit()
    conn.close()


def auth_user(login, password):
    conn = sqlite3.connect("fcb.db")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    
def add_citizens(name,surname, patronymic,is_wanted):
    conn = sqlite3.connect("fcb.db")


def add_user(login, password):
    ...

def is_user_exists(login):
    conn = sqlite3.connect("fcb.db")
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE login = ?", (login,))
    user = cursor.fetchone()

if __name__ == "__main__":
    create_db()
    add_citizens("tIMUR", "sHUPOAWLDKAWLJKD", "HZ", 1)
    users = get_users()
    users = get_users()