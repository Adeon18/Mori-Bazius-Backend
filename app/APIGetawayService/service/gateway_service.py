from common.game_data.stats import Stats
from common.game_data.resources import Resources
from common.game_data.user import User
from kafka import KafkaProducer

import requests

import json

KAFKA_SERVER = 'kafka-server:9092'
GAME_DATA_TOPIC = 'game-data'
GAME_STATS_TOPIC = 'game-stats'

REGISTER_SERVICE_URL = 'http://register-service:8080/user/'
LOGIN_SERVICE_URL = 'http://login-service:8080/login/user/'
VALIDATION_SERVICE_URL = 'http://validation-service:8080/validate/'

STATS_GAME_DATA_URL = 'http://game_data:8000/stats?player_id='
RESOURCES_GAME_DATA_URL = 'http://game_data:8000/resources?player_id='
LEADERBOARD_URL = "http://game_data:8000/leaderboard?limit="


class GatewayService:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])

    # Returns a boolean whether the validation was successful
    def verify_request(self, uid: str, token: str):
        response = requests.post(
            url=VALIDATION_SERVICE_URL, json={"uid": uid, "token": token})

        if response.text == "true":
            return True

        return False

    def handle_register_operation(self, user_data: User):
        response = requests.post(
            url=REGISTER_SERVICE_URL, json={"username": user_data.username, "password": user_data.password})

        return response.text

    def handle_login_operation(self, user_data: User):
        response = requests.post(
            url=LOGIN_SERVICE_URL, json=dict(user_data))

        return response.text

    def get_game_resources(self, player_id: int):
        response = requests.get(url=RESOURCES_GAME_DATA_URL + str(player_id))

        return response.json()

    def set_game_resources(self, player_id: int, resources: Resources):
        # Verify the sender
        if (not self.verify_request(resources.player_id, resources.token)):
            print("Bad token: " + resources.token, flush=True)
            return {"success": False}

        resources.token = None

        # sync for now
        metadata = self.producer.send(GAME_DATA_TOPIC, json.dumps(
            resources.dict()).encode()).get(timeout=10)

        return {"success": True, "topic": metadata.topic}

    def get_game_stats(self, player_id: int):
        response = requests.get(url=STATS_GAME_DATA_URL + str(player_id))

        return response.json()

    def set_game_stats(self, player_id: int, stats: Stats):
        # Verify the sender
        if (not self.verify_request(stats.player_id, stats.token)):
            print("Bad token: " + stats.token, flush=True)
            return {"success": False}

        stats.token = None

        # set gata in game_data
        metadata = self.producer.send(GAME_STATS_TOPIC, json.dumps(
            stats.dict()).encode()).get(timeout=10)

        return {"success": True, "topic": metadata.topic}

    def get_game_leaderboard(self, limit):
        response = requests.get(url=LEADERBOARD_URL + str(limit))

        return response.json()
