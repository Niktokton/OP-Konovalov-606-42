import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('scores.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                player1 TEXT,
                result TEXT,
                player2 TEXT
            )
        ''')
        self.conn.commit()

    def save_score(self, player1, result, player2):
        self.cursor.execute('INSERT INTO scores (player1, result, player2) VALUES (?, ?, ?)', (player1, result, player2))
        self.conn.commit()

    def get_scores(self, limit=15):
        self.cursor.execute('SELECT * FROM scores ORDER BY ROWID DESC LIMIT ?', (limit,))
        return self.cursor.fetchall()