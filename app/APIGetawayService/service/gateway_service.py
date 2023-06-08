from common.game_data.stats import Stats
from common.game_data.resources import Resources
from common.game_data.user import User
from common.game_data.guild import GuildCreation, Member

from kafka import KafkaProducer

import requests
import consul
import json
import random

KAFKA_SERVER = 'kafka-server:9092'
GAME_DATA_TOPIC = 'game-data'
GAME_STATS_TOPIC = 'game-stats'

REGISTER_SERVICE_URL = 'http://register-service:8080/user/'
LOGIN_SERVICE_URL = 'http://login-service:8080/login/user/'
VALIDATION_SERVICE_URL = 'http://validation-service:8080/c/'

STATS_GAME_DATA_URL = 'http://game_data:8000/stats?player_id='
RESOURCES_GAME_DATA_URL = 'http://game_data:8000/resources?player_id='
LEADERBOARD_URL = "http://game_data:8000/leaderboard?limit="
AVERAGE_GAME_DATA_URL = 'http://game_data:8000/resources?player_id='

# Guilds service urls
GUILDS_URL = "http://guilds-service:6969/guilds?limit={}"
GUILD_MEMBERS_URL = "http://guilds-service:6969/members?gid={}"
GUILD_BY_MEMBER_URL = "http://guilds-service:6969/guild?player_id={}"
CREATE_GUILD_URL = "http://guilds-service:6969/guilds/new"
JOIN_GUILD_URL = "http://guilds-service:6969/guilds/members/new"
LEAVE_GUILD_URL = "http://guilds-service:6969/guilds/leave?gid={}&player_id={}"
DELETE_GUILD_URL = "http://guilds-service:6969/guilds/delete?gid={}"


class GatewayService:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])
        self.consul_service = consul.Consul(host="consul")

    # Returns a boolean whether the validation was successful
    def verify_request(self, uid: str, token: str):
        url, port = self.get_address("validation")
        response = requests.post(
            url=f"http://{url}:{port}/validate", json={"uid": uid, "token": token})

        if response.text == "true":
            return True

        return False

    def get_address(self, service_name):
        consul_info = self.consul_service.health.service(service_name)[1]
        address = random.choice(consul_info)["Service"]["Address"]
        port = random.choice(consul_info)["Service"]["Port"]
        return address, port

    def handle_register_operation(self, user_data: User):
        response = requests.post(
            url=REGISTER_SERVICE_URL, json={"username": user_data.username, "password": user_data.password})

        return response.json()

    def handle_login_operation(self, user_data: User):
        response = requests.post(
            url=LOGIN_SERVICE_URL, json=dict(user_data))

        return response.json()

    def get_game_resources(self, player_id: int):
        url, port = self.get_address("game-data")
        response = requests.get(url=f'http://{url}:{port}/resources?player_id=' + str(player_id))

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
        url, port = self.get_address("game-data")
        response = requests.get(url=f"http://{url}:{port}/stats?player_id=" + str(player_id))

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
        url, port = self.get_address("game-data")
        response = requests.get(url=f"http://{url}:{port}/leaderboard?limit={limit}")

        return response.json()

    def get_game_data_average(self, player_id: int):
        url, port = self.get_address("game-data")
        response = requests.get(url=f'http://{url}:{port}/resources?player_id=' + str(player_id))

        return response.json()

    def get_guilds(self, limit: int):
        response = requests.get(GUILDS_URL.format(limit))
        return response.json()

    def get_members(self, gid: str):
        response = requests.get(GUILD_MEMBERS_URL.format(gid))
        return response.json()

    def get_guild_by_member(self, player_id: int):
        response = requests.get(GUILD_BY_MEMBER_URL.format(player_id))
        return response.json()

    def create_guild(self, new_guild: GuildCreation):
        print(new_guild)
        response = requests.post(CREATE_GUILD_URL, json=new_guild)
        return response.json()

    def join_guild(self, member: Member):
        response = requests.post(JOIN_GUILD_URL, json=member.dict())
        return response.json()

    def leave_guild(self, gid: str, player_id: int):
        response = requests.delete(LEAVE_GUILD_URL.format(gid, player_id))
        return response.json()

    def delete_guild(self, gid: str):
        response = requests.delete(DELETE_GUILD_URL.format(gid))
        return response.json()

