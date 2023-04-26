from aiokafka import AIOKafkaConsumer
import asyncio
import os

from repository.game_data_repository import GameDataRepository
from repository.cassandra_repository import CassandraRepository

from common.game_data.resources import Resources
from common.game_data.stats import Stats

class GameDataService:
    def __init__(self, repo: GameDataRepository) -> None:
        self.repo = repo
        kafka_address = os.getenv("KAFKA_ADDRESS")
        kafka_address = kafka_address if kafka_address is not None else "localhost:29092"
        print("Hello from constructor")
        self.event_loop = asyncio.get_event_loop()
        self.data_consumer = AIOKafkaConsumer("game-data", loop=self.event_loop, bootstrap_servers=kafka_address)
        self.stats_consumer = AIOKafkaConsumer("game-stats", loop=self.event_loop, bootstrap_servers=kafka_address)
    
    def new_service_with_cassandra():
        return GameDataService(CassandraRepository())

    def get_stats(self, player_id: int) -> Stats:
        stats = self.repo.get_stats(player_id)
        return Stats.parse_obj(stats)

    def get_resources(self, player_id: int) -> Resources:
        resources = self.repo.get_resources(player_id)
        return Resources.parse_obj(resources)

    def set_stats(self, player_id: int, stats: Stats):
        self.repo.set_stats(player_id, stats)

    def set_resources(self, player_id: int, resources: Resources):
        self.repo.set_resources(player_id, resources)
    
    async def consume_data(self):
        await self.data_consumer.start()

        try:
            async for msg in self.data_consumer:
                print("consumed data")
        finally:
            await self.data_consumer.stop()

    async def consume_stats(self):
        await self.stats_consumer.start()

        try:
            async for msg in self.stats_consumer:
                print("consumed stats")
        finally:
            await self.stats_consumer.stop()

    def create_consume_stats_task(self):
        self.event_loop.create_task(self.consume_stats())
        
    def create_consume_data_task(self):
        self.event_loop.create_task(self.consume_data())

    async def shutdown_consumers(self):
        await self.data_consumer.stop()
        await self.stats_consumer.stop()
