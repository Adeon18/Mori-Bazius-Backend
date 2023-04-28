from User import User
from LoginRepositoryPostgress import LoginRepositoryPostgress
import requests

class LoginService:
    def __init__(self):
        self.repository = LoginRepositoryPostgress()

    def try_login_user(self, user: User):
        uid = self.repository.get_user_uid(user)[0]
        if uid != -1:
            print(f"user exists, uid {uid}")
            response = requests.post(url="http://validation-service:8080/log/" + str(uid))
            token = response.text
            print(token)
            return token
        else:
            print("incorrect credentials")
            return 401
