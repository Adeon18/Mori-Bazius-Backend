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
        def post_user(user: User):
            token = self.service.try_login_user(user)
            if token == 401:
                raise HTTPException(status_code=401, detail="Invalid Credentials")
            else:
                return token


controller = LoginController()

if __name__ == "__main__":
    uvicorn.run(controller.app, port=8080, host="0.0.0.0")
