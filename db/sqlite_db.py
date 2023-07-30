import sqlite3


def start_sql():
    global base, cur
    base = sqlite3.connect('db.sqlite3')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS info(name TEXT, content TEXT)')
    base.commit()


async def add_update_content(state):
    async with state.proxy() as data:
        if not cur.execute(
            'SELECT * FROM info WHERE name = ?', (data['name'],)
        ).fetchone():
            cur.execute('INSERT INTO info VALUES (?, ?)', tuple(data.values()))
        else:
            cur.execute(
                'UPDATE info SET content = ? WHERE name = ?',
                (data['content'], data['name'])
            )
        base.commit()


async def get_content(name):
    cur.execute('SELECT content FROM info WHERE name = ?', (name,))
    for result in cur:
        return result[0]
