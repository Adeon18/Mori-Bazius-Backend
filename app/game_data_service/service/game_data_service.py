from aiokafka import AIOKafkaConsumer
import asyncio
import os
import consul
import socket

from repository.game_data_repository import GameDataRepository
from repository.cassandra_repository import CassandraRepository

from common.game_data.resources import Resources
from common.game_data.stats import Stats

class GameDataService:
    def __init__(self, repo: GameDataRepository) -> None:
        self.repo = repo
        kafka_address = os.getenv("KAFKA_ADDRESS", "localhost:29092")

        self.consul_service = consul.Consul(host="consul")
        hostname = socket.gethostname()
        self.id = os.environ["SERVICE_ID"]
        check = consul.Check.http(f"http://{hostname}:8000/health", "10s", "2s", "20s")
        self.name = "game-data"
        self.consul_service.agent.service.register(self.name, service_id=self.name + self.id, address=hostname,
                                                   port=8000, check=check)
        
        self.event_loop = asyncio.get_event_loop()
        self.data_consumer = AIOKafkaConsumer("game-data", loop=self.event_loop, bootstrap_servers=kafka_address, group_id="game_data_consumer", auto_offset_reset="earliest", enable_auto_commit=True)
        self.stats_consumer = AIOKafkaConsumer("game-stats", loop=self.event_loop, bootstrap_servers=kafka_address, group_id="game_data_consumer", auto_offset_reset="earliest", enable_auto_commit=True)
    
    def new_service_with_cassandra():
        return GameDataService(CassandraRepository())

    def get_stats(self, player_id: int) -> Stats:
        stats = self.repo.get_stats(player_id)
        return Stats.parse_obj(stats)

    def get_resources(self, player_id: int) -> Resources:
        resources = self.repo.get_resources(player_id)
        return Resources.parse_obj(resources)

    def set_stats(self, player_id: int, stats: Stats):
        old_stats = self.get_stats(stats.player_id)
        if stats.power is not None and old_stats.power is not None and old_stats.power != stats.power:
            for field_name, field_val in vars(stats).items():
                if not callable(field_val) and field_val is None:
                    setattr(stats, field_name, getattr(old_stats, field_name))
            self.delete_stats(old_stats)

        self.repo.set_stats(stats.player_id, stats)

    def set_resources(self, player_id: int, resources: Resources):
        self.repo.set_resources(player_id, resources)
    
    def delete_stats(self, stats: Stats):
        self.repo.delete_stats(stats)
    
    async def consume_data(self):
        await self.data_consumer.start()

        try:
            async for msg in self.data_consumer:
                print(f"consumed data: {msg.value.decode('utf-8')}")
                resources = Resources.parse_raw(msg.value)
                self.set_resources(resources.player_id, resources)
        finally:
            await self.data_consumer.stop()

    async def consume_stats(self):
        await self.stats_consumer.start()

        try:
            async for msg in self.stats_consumer:
                print(f"consumed stats: {msg.value.decode('utf-8')}")
                stats = Stats.parse_raw(msg.value)
                self.set_stats(stats.player_id, stats)
        finally:
            await self.stats_consumer.stop()

    def create_consume_stats_task(self):
        self.event_loop.create_task(self.consume_stats())
        
    def create_consume_data_task(self):
        self.event_loop.create_task(self.consume_data())

    async def shutdown_consumers(self):
        await self.data_consumer.stop()
        await self.stats_consumer.stop()

    def get_leaderboard(self, limit: int):
        return self.repo.get_leaderboard(limit)

    def get_average_resources(self, player_id: int):
        return self.repo.get_average_resources(player_id)
