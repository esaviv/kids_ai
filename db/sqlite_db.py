import sqlite3


def start_sql():
    global base, cur
    base = sqlite3.connect('kids_ai.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS info(name TEXT, content TEXT)')
    base.commit()
