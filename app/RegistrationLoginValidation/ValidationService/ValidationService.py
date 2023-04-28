from User import User
from ValidationRepositoryInMemory import ValidationRepositoryInMemory
import secrets


class ValidationService:
    def __init__(self):
        self.repository = ValidationRepositoryInMemory()

    def log_user(self, uid):

        token = secrets.token_hex(20)
        self.repository.add_user_token(uid, token)
        return token

    def validate_user(self, uid, token):
        stored_token = self.repository.get_user_token(uid)
        if token == stored_token and stored_token != "none":
            return True
        else:
            return False
