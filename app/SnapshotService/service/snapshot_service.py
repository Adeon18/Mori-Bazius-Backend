import asyncio
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))  # I LOVE PYTHON

from repository.snapshot_service_repository import SnapshotServiceRepository
from contextlib import asynccontextmanager
from fastapi import FastAPI
from datetime import datetime, timedelta


class SnapShotService:
    def __init__(self):
        self.repo = SnapshotServiceRepository()

    def get_last_N_minute_stats(self, player_id: int, N: int):
        current_time = datetime.now()
        end_time = current_time.strftime("%Y-%m-%d-%H-%M")

        time_minus_N = current_time - timedelta(minutes=N)
        start_time = time_minus_N.strftime("%Y-%m-%d-%H-%M")

        return self.repo.get_last_stat_logs_player_id_range(player_id, start_time, end_time)

    def get_last_N_minute_resources(self, player_id: int, N: int):
        current_time = datetime.now()
        end_time = current_time.strftime("%Y-%m-%d-%H-%M")

        time_minus_N = current_time - timedelta(minutes=N)
        start_time = time_minus_N.strftime("%Y-%m-%d-%H-%M")

        return self.repo.get_last_resource_logs_player_id_range(player_id, start_time, end_time)

    async def make_stat_snapshot(self):
        while True:
            current_time = datetime.now()
            time_string = current_time.strftime("%Y-%m-%d-%H-%M")

            # Add your processing logic here
            stats = self.repo.get_all_stats()
            for stat in stats:
                stat["time"] = time_string
            self.repo.add_stat_snapshot(stats)
            print("Added stats snapshit at " + time_string)

            await asyncio.sleep(120)  # Sleep for 2 minutes (120 seconds)

    async def make_resource_snapshot(self):
        while True:
            current_time = datetime.now()
            time_string = current_time.strftime("%Y-%m-%d-%H-%M")
            # Add your processing logic here
            resources = self.repo.get_all_resources()
            for res in resources:
                res["time"] = time_string
            self.repo.add_resource_snapshot(resources)
            print("Added resource snapshit at " + time_string)

            await asyncio.sleep(120)  # Sleep for 2 minutes (120 seconds)

    async def delete_old_stat_snapshot(self):
        while True:
            current_time = datetime.now()

            time_minus_N = current_time - timedelta(minutes=120)
            time = time_minus_N.strftime("%Y-%m-%d-%H-%M")

            self.repo.delete_old_stats_snapshots(time)

            print("Deleted stat snapshots that are older than 120 mins")

            await asyncio.sleep(7200)  # Sleep for 2 hours (7200 seconds)

    async def delete_old_resource_snapshot(self):
        while True:
            current_time = datetime.now()

            time_minus_N = current_time - timedelta(minutes=120)
            time = time_minus_N.strftime("%Y-%m-%d-%H-%M")

            self.repo.delete_old_resource_snapshots(time)

            print("Deleted resource snapshots that are older than 120 mins")

            await asyncio.sleep(7200)  # Sleep for 2 hours (7200 seconds)