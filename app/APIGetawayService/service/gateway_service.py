from common.game_data.stats import Stats
from common.game_data.resources import Resources
from kafka import KafkaProducer

import json

KAFKA_SERVER = 'kafka-server:9092'
GAME_DATA_TOPIC = 'game-data'
GAME_STATS_TOPIC = 'game-stats'


class GatewayService:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])

    def get_game_resources(self, player_id: int):
        # Verify the sender
        # get gata from game_data
        return {"player_id": player_id}

    def set_game_resources(self, player_id: int, resources: Resources):
        # Verify the sender

        # sync for now
        metadata = self.producer.send(GAME_DATA_TOPIC, json.dumps(
            resources.dict()).encode()).get(timeout=10)

        return metadata

    def get_game_stats(self, player_id: int):
        # Verify the sender
        # get gata from game_data
        return {"player_id": player_id}

    def set_game_stats(self, player_id: int, stats: Stats):
        # Verify the sender
        # set gata in game_data
        # sync for now
        metadata = self.producer.send(GAME_STATS_TOPIC, json.dumps(
            stats.dict()).encode()).get(timeout=10)

        return metadata

    def get_game_leagueboard(self, limit):
        return {"limit": limit}
