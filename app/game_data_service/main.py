import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # I LOVE PYTHON

import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager

from service.game_data_service import GameDataService
from common.game_data.stats import Stats
from common.game_data.resources import Resources


service = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    service = GameDataService.new_service_with_cassandra()
    service.create_consume_data_task()
    service.create_consume_stats_task()

    yield

    # Shutdown
    print("Shutdown event")
    await service.shutdown_consumers()

app = FastAPI(lifespan=lifespan)


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
