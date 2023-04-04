import sqlite3
import time, datetime


start = time.time()


class Save(object):

    def __init__(self):
        self.conn = self.creation_save()
        self.conn.close()

    def creation_save(self):
        try:
            conn = sqlite3.connect('archive.sqlite')
            cur = conn.cursor()
            cur.execute(''' DROP TABLE IF EXISTS archive ''')
            cur.execute(''' CREATE TABLE IF NOT EXISTS archive(
                                id INT PRIMARY KEY,
                                file_name TEXT,
                                date_solved DATE
                                time_to_solve REAL);''')
            return conn
        except IOError as e:
            print(e)

    def add_solved(self, task):
        con = sqlite3.connect('archive.sqlite')
        sql = ''' INSERT INTO archive(file_name, date_solved, time_execute)
                    VALUES (?,?,?)'''
        cur = con.cursor()
        cur.execute(sql, task)
        con.commit()
        con.close()

    def display_database(self):
        con = sqlite3.connect('archive.sqlite')
        sql = ''' SELECT * FROM archive '''
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        con.close()

    def close(self):
        self.conn.close()

t1 = time.time()-start
print(t1)

table = Save()
table.display_solve()
table.add_solved(("maze_1", datetime.date.today(), t1))