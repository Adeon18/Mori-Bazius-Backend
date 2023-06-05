import asyncio
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))  # I LOVE PYTHON

from service.snapshot_service import SnapShotService
from contextlib import asynccontextmanager
from fastapi import FastAPI

service = SnapShotService()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    asyncio.get_event_loop().create_task(service.make_stat_snapshot())
    asyncio.get_event_loop().create_task(service.make_resource_snapshot())
    asyncio.get_event_loop().create_task(service.delete_old_stat_snapshot())
    asyncio.get_event_loop().create_task(service.delete_old_resource_snapshot())
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/logged_stats")
async def logged_stats(player_id: int, last_minutes: int):
    return service.get_last_N_minute_stats(player_id, last_minutes)

@app.get("/logged_resources")
async def logged_resources(player_id: int, last_minutes: int):
    return service.get_last_N_minute_resources(player_id, last_minutes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9010)
