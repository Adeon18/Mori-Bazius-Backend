from fastapi import FastAPI

from service.game_data_service import GameDataService

from domain.stats import Stats
from domain.resources import Resources

app = FastAPI()

service = GameDataService.new_service_with_cassandra()

@app.get("/stats")
async def stats(player_id: int):
    return service.get_stats(player_id)

@app.post("/stats")
async def update_stats(player_id: int, stats: Stats):
    service.set_stats(player_id, stats)
    return stats
    

@app.get("/resources")
async def resources(player_id: int):
    return service.get_resources(player_id)

@app.post("/resources")
async def update_resources(player_id: int, resources: Resources):
    service.set_resources(player_id, resources)
    return resources