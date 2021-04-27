import sqlite3

def database_init():
    database = sqlite3.connect("data/scores.db")
    try:
        database.execute("CREATE TABLE Scores (id INTEGER PRIMARY KEY, score INTEGER)")
    except:
        pass

if __name__ == "__main__":
    database_init()