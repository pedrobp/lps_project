import psycopg2


class Processor():
    __conn = None

    def __init__(self):
        self.connect()
        # self.test_conn()

    def connect(self):
        self.__conn = psycopg2.connect(
            "host=localhost dbname=postgres user=postgres password=123456")

    def test_conn(self):
        cur = self.__conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        data = cur.fetchall()
        print(data)

    def save_push(self, p_obj):
        cur = self.__conn.cursor()

        for commit in p_obj['commits']:
            query = "INSERT INTO public.push_log VALUES (DEFAULT, '" +\
                "', '".join([p_obj['pusher']['name'], p_obj['pusher']['email'], str(p_obj['sender']['id']),
                             p_obj['repository']['name'], p_obj['after'], p_obj['ref'], str(commit['id']),
                             commit['message'], commit['timestamp'], commit['url'], commit['author']['username'],
                             ", ".join(commit['modified']), ", ".join(commit['added']), ", ".join(commit['removed'])]) +\
                "')"

            cur.execute(query)
            self.__conn.commit()
            cur.close()
            self.__conn.close()

            print("Successfully inserted into the database")
