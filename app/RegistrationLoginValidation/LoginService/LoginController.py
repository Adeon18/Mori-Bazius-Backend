from fastapi import FastAPI
import uvicorn
from User import User
from LoginService import LoginService
from fastapi import FastAPI, HTTPException


class LoginController:
    def __init__(self):
        self.app = FastAPI()
        self.service = LoginService()

        @self.app.post("/login/user/")
        def login_user(user: User):
            logged_user = self.service.try_login_user(user)
            return logged_user


controller = LoginController()

if __name__ == "__main__":
    uvicorn.run(controller.app, port=8080, host="0.0.0.0")
