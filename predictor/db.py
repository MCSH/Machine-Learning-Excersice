import sqlite3

def process(row):
    return (row[0],(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))

class DB():
    def __init__(self):
        conn = sqlite3.connect('database.db')

        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS input_data
                    (id INTEGER PRIMARY KEY, p1 REAL, p2 REAL, p3 REAL, p4 REAL, p5 REAL, p6 REAL, p7 REAL, p8 REAL, p9 REAL, p10 REAL, p11 REAL, p12 REAL, p13 REAL)''')

        c.execute('''CREATE TABLE IF NOT EXISTS output_data
                     (id INTEGER, target INTEGER PRIMARY KEY)''')

        conn.commit()

        self.conn = conn

    def read(self):
        c = self.conn.cursor()
        sql_statement = """
        select id,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13 FROM input_data
        """

        rc = c.execute(sql_statement)
        for row in rc:
            yield process(row)

    def write(self, id, y):
        c = self.conn.cursor()
        sql_statement = 'insert into output_data(id, target) values(?,?)'
        c.execute(sql_statement, (id, y))
