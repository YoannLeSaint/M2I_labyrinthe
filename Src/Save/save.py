import sqlite3
import time, datetime


start = time.time()


class Save(object):

    def __init__(self):
        self.conn = self.creation_save()
    def creation_save(self):
        try:
            conn = sqlite3.connect('archive.sqlite')
            cur = conn.cursor()
            #cur.execute(''' DROP TABLE IF EXISTS archive ''')
            cur.execute(''' CREATE TABLE IF NOT EXISTS archive(
                                id INT PRIMARY KEY,
                                file_name TEXT,
                                date_solved DATE,
                                time_execute REAL);''')
            return conn
        except IOError as e:
            print(e)

    def add_solved(self, task):
        sql = ''' INSERT INTO archive(file_name, date_solved, time_execute)
                    VALUES (?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(sql, task)
        self.conn.commit()
        return cur.lastrowid

    def display_database(self):
        print("Mazes database")
        sql = ''' SELECT file_name, date_solved, time_execute FROM archive '''
        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    def delete(self):
        cur = self.conn.cursor()
        cur.execute(''' DROP TABLE IF EXISTS archive ''')
        self.creation_save()



    def close(self):
        self.conn.close()




# t1 = time.time()-start
# print(t1)
#
# table = Save()
# table.add_solved(("maze_1", datetime.date.today(), t1))
# table.add_solved(("maze_2", datetime.date.today(), t1+1))
# table.display_database()
# table.delete()
# print('_________________')
# table.display_database()
# table.close()