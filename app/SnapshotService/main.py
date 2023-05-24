import asyncio
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))  # I LOVE PYTHON

from repository.SnapshotServiceRepository import SnapshotServiceRepository
from contextlib import asynccontextmanager
from fastapi import FastAPI
from datetime import datetime

rep = SnapshotServiceRepository();

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    asyncio.get_event_loop().create_task(make_snapshot())

    yield



app = FastAPI(lifespan=lifespan)


async def make_snapshot():
    while True:
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d-%H-%M")

        # Add your processing logic here
        stats = rep.get_all_stats()
        for stat in stats:
            stat["time"] = time_string
        rep.add_stat_snapshot(stats)
        print("Added stats snapshit at " + time_string)

        # Add your processing logic here
        resources = rep.get_all_resources()
        for res in resources:
            res["time"] = time_string
        rep.add_resource_snapshot(resources)
        print("Added resource snapshit at " + time_string)

        await asyncio.sleep(60)  # Sleep for 2 minutes (120 seconds)


@app.get("/a")
async def kills():
    return {"a": 1}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9010)
