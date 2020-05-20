import psycopg2

class Processor():
    __conn = None

    def connect(self):
        self.__conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123456")

    def test_conn(self):
        cur = self.__conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        data = cur.fetchall()
        print(data)

    def save_push(self, push_object):
        print("Got push with: {0}".format(push_object))

db = Processor()
db.connect()
db.test_conn()

    