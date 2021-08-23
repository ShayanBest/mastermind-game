import sqlite3
from tkinter import messagebox

def create():
    try:
        sqlite_connection = sqlite3.connect('Game.db')
        cursor = sqlite_connection.cursor()

        query = """
            CREATE TABLE IF NOT EXISTS scorelist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                level TEXT NOT NULL,
                time TEXT  NOT NULL
            );
        """
        cursor.execute(query)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as err:
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def insert(name, level, time):
    try:
        sqlite_connection = sqlite3.connect('Game.db')
        cursor = sqlite_connection.cursor()

        query = """
        INSERT INTO scorelist (name, level, time)
        VALUES (?,?,?);
        """
        val = name, level, time
        cursor.execute(query,val)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as err:
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def select():
    try:
        sqlite_connection = sqlite3.connect('Game.db')
        cursor = sqlite_connection.cursor()

        query = """
        SELECT name, level, time
        FROM scorelist;
        """

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as err:
        return False
    else:
        return result
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def init(scorelist):
    result = create()
    if result == False:
        messagebox.showerror("Error","database Error")  
        return
    
    result = select()
    if result == False:
        messagebox.showerror("Error","database Error")  
        return

    for data in result:
        scorelist.insert(0 , " - ".join(data))  

def save_data_to_database(name,level,time,scorelist):
        
    result = insert(name,level,time)

    if result == False:
        messagebox.showerror("Error","database Error")  
        return








