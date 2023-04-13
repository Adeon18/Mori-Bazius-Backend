import datetime

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Union
import psycopg2


class User(BaseModel):
    username: str
    password: str
    uid: Union[int, None] = None
    created_on: Union[datetime.datetime, None] = None


class RegisterController:
    def __init__(self):
        self.app = FastAPI()

        self.conn = psycopg2.connect(database="users",
                                     host="postgresql",
                                     user="admin",
                                     password="admin",
                                     port="5432")

        self.cursor = self.conn.cursor()
        print("connected")

        @self.app.get("/user/{uid}")
        def get_user(uid: int) -> User:
            self.cursor.execute(f"SELECT * FROM users WHERE uid={uid}")
            self.conn.commit()
            result = self.cursor.fetchone()
            print(result)
            user = User(uid=result[0], username=result[1], password=result[2], created_on=result[3])
            # user.uid = result[0]
            # user.username = result[1]
            # user.password = result[2]
            # user.created_on = result[3]
            return user

        @self.app.post("/user")
        def post_user(user: User) -> int:
            self.cursor.execute(f"INSERT INTO users(username, password, created_on) VALUES ('{user.username}', '{str(user.password)}', current_timestamp) RETURNING uid")
            self.conn.commit()
            result = self.cursor.fetchone()
            print(result[0])
            return result[0]


controller = RegisterController()

if __name__ == "__main__":
    uvicorn.run(controller.app, port=8080, host="0.0.0.0")