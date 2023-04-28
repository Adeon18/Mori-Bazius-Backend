from User import User
import psycopg2


class LoginRepositoryPostgress:
    def __init__(self):
        self.conn = psycopg2.connect(database="users",
                                     host="postgresql",
                                     user="admin",
                                     password="admin",
                                     port="5432")
        self.cursor = self.conn.cursor()
        print("connected")

    def get_user_uid(self, user: User):
        self.cursor.execute(f"SELECT * FROM users WHERE username='{user.username}' AND password='{user.password}'")
        res = self.cursor.fetchone()
        if res is None:
            return -1
        else:
            return res
