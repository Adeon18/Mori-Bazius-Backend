from User import User, UidTok
from LoginRepositoryPostgress import LoginRepositoryPostgress
from fastapi import HTTPException
import requests

class LoginService:
    def __init__(self):
        self.repository = LoginRepositoryPostgress()

    def try_login_user(self, user: User) -> UidTok:
        uid = self.repository.get_user_uid(user)
        if uid is not None:
            uid = uid[0]
            print(f"user exists, uid {uid}")
            response = requests.post(url="http://validation-service:8080/log/" + str(uid))
            token = response.text
            print(token)
            return UidTok(uid=uid, token=token)
        else:
            print("incorrect credentials")
            raise HTTPException(status_code=401, detail="Invalid Credentials")