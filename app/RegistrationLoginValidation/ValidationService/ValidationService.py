from User import User
from ValidationRepositoryInMemory import ValidationRepositoryInMemory
import secrets
import consul
import os
import socket


class ValidationService:
    def __init__(self):
        self.repository = ValidationRepositoryHaz()
        hostname = socket.gethostname()
        check = consul.Check.http(f"http://{hostname}:8080/health", "10s", "2s", "20s")
        self.consul_service.agent.service.register(self.name, service_id=self.name + self.id, address=hostname,
                                                   port=8080, check=check)
        self.logging_repository.add_map_name(self.consul_service.kv.get('map-name')[1]["Value"].decode('utf-8'))

    def log_user(self, uid):
        token = secrets.token_hex(20)
        self.repository.add_user_token(uid, token)
        return token

    def validate_user(self, uid, token):
        stored_token = self.repository.get_user_token(uid)
        return token == stored_token and stored_token != "none"
