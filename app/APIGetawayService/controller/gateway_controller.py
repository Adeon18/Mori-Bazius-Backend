from fastapi import FastAPI
from service.gateway_service import GatewayService
from domain.stats import Stats
from domain.resources import Resources


class App:
    def __init__(self):
        self.app = FastAPI()
        self.service = GatewayService()

        @self.app.get("/game_data/stats")
        async def game_data_stats(player_id: int):
            return self.service.get_game_stats(player_id)

        @self.app.post("/game_data/stats")
        async def game_data_set_stats(player_id: int, stats: Stats):
            return self.service.set_game_stats(player_id, stats)

        @self.app.get("/game_data/resources")
        async def game_data_resources(player_id: int):
            return self.service.get_game_resources(player_id)

        @self.app.get("/game_data/resources")
        async def game_data_set_resources(player_id: int, resources: Resources):
            return self.service.set_game_resources(player_id, resources)
