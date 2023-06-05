from fastapi import FastAPI
import uvicorn
from User import UidTok
from ValidationService import ValidationService
from pydantic import BaseModel


class LoginController:
    def __init__(self):
        self.app = FastAPI()
        self.service = ValidationService()

        @self.app.post("/log/{uid}")
        def post_user(uid: int):
            token = self.service.log_user(uid)
            return token

        @self.app.post("/validate")
        def validate_user(user: UidTok) -> bool:
            res = self.service.validate_user(user.uid, user.token)
            return res

        @self.app.get("/health")
        def health_check():
            return True


controller = LoginController()

if __name__ == "__main__":
    uvicorn.run(controller.app, port=8080, host="0.0.0.0")
