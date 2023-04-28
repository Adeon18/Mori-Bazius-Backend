from User import User
import psycopg2


class ValidationRepositoryInMemory:
    def __init__(self):
        self.logged_users = dict()

    def add_user_token(self, uid, token):
        self.logged_users[uid] = token

    def get_user_token(self, uid):
        if uid in self.logged_users.keys():
            return self.logged_users[uid]
        else:
            return "none"
