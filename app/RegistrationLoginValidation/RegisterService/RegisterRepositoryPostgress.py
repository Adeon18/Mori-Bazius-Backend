from User import User
import psycopg2
from fastapi import HTTPException

class RegisterRepositoryPostgress:
    def __init__(self):
        self.conn = psycopg2.connect(database="users",
                                     host="postgresql",
                                     user="admin",
                                     password="admin",
                                     port="5432")
        self.cursor = self.conn.cursor()
        print("connected")

    def register_user(self, user: User):
        self.cursor.execute(f"SELECT exists (SELECT 1 FROM users WHERE username='{user.username}')")
        if self.cursor.fetchone()[0]:
            raise HTTPException(status_code=409, detail="user already exists")
        self.cursor.execute(
            f"INSERT INTO users(username, password, created_on) VALUES ('{user.username}', '{str(user.password)}',\
             current_timestamp) RETURNING uid")
        self.conn.commit()
        return self.cursor.fetchone()

    def del_user(self, uid):
        pass

    def get_user(self, uid):
        self.cursor.execute(f"SELECT * FROM users WHERE uid={uid}")
        self.conn.commit()
        return self.cursor.fetchone()
