from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    level: int = 0
    guild_name: Union[str, None] = None


class MyServer:
    def __init__(self):
        self.app = FastAPI()

        self.users = dict()
        self.last_id = 0

        @self.app.get("/users/{uid}")
        def get_user_by_id(uid: int) -> User:
            print("AAAA")
            print(self.users[uid])
            return self.users[uid]

        @self.app.post("/users")
        def post_user(user: User) -> int:
            self.last_id += 1
            self.users[self.last_id] = user
            return self.last_id


server = MyServer()
