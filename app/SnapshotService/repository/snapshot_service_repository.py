import os
from collections import namedtuple
from cassandra.cluster import Cluster


class SnapshotServiceRepository():
    def __init__(self) -> None:
        cassandra_endpoint = os.getenv("CASSANDRA_ENDPOINT", "localhost")
        cassandra_port = os.getenv("CASSANDRA_PORT", 9042)

        self.cassandra_client = Cluster(
            [cassandra_endpoint], port=cassandra_port)
        self.session = self.cassandra_client.connect()

    def get_last_stat_logs_player_id_range(self, player_id: int, start_time: str, end_time: str) -> dict:
        query = f"""
        SELECT * FROM hunters.player_stats_by_player_id_and_time_logs WHERE player_id = {player_id} AND time < '{end_time}' AND time > '{start_time}'"""
        res = self.session.execute(query)
        json = []
        for row in res:
            result = {}
            for column in row._fields:
                result[column] = getattr(row, column)
            json.append(result)

        return json

    def get_last_resource_logs_player_id_range(self, player_id: int, start_time: str, end_time: str) -> dict:
        query = f"""
        SELECT * FROM hunters.game_data_by_player_id_and_time_logs WHERE player_id = {player_id} AND time < '{end_time}' AND time > '{start_time}'"""
        res = self.session.execute(query)
        json = []
        for row in res:
            result = {}
            for column in row._fields:
                result[column] = getattr(row, column)
            json.append(result)

        return json

    # Get stats for all players
    def get_all_stats(self) -> dict:
        query = f"""
        SELECT * FROM hunters.player_stats_by_player_id"""
        res = self.session.execute(query)
        json = []
        for row in res:
            result = {}
            for column in row._fields:
                result[column] = getattr(row, column)
            json.append(result)

        return json

    # Get resources for all players
    def get_all_resources(self) -> dict:
        query = f"""
        SELECT * FROM hunters.game_data_by_player_id"""
        res = self.session.execute(query)
        json = []
        for row in res:
            result = {}
            for column in row._fields:
                result[column] = getattr(row, column)
            json.append(result)

        return json

    # Insert all data updated with time into the logs
    # TODO: Make it a batch insert
    def add_stat_snapshot(self, stat_list: list):
        for stat_entry in stat_list:
            keys_to_update = list(stat_entry.keys())
            values_to_update = [stat_entry[key] for key in keys_to_update]

            query = f"""
            INSERT INTO hunters.player_stats_by_player_id_and_time_logs
            ({", ".join(keys_to_update)}) VALUES ({", ".join(["?" for _ in values_to_update])})
            """
            query = self.session.prepare(query)

            self.session.execute(query, values_to_update)

    # Insert all data updated with time into the logs
    # TODO: Make it a batch insert
    def add_resource_snapshot(self, res_list: list):
        for stat_entry in res_list:
            keys_to_update = list(stat_entry.keys())
            values_to_update = [stat_entry[key] for key in keys_to_update]

            query = f"""
            INSERT INTO hunters.game_data_by_player_id_and_time_logs
            ({", ".join(keys_to_update)}) VALUES ({", ".join(["?" for _ in values_to_update])})
            """
            query = self.session.prepare(query)

            self.session.execute(query, values_to_update)

    def delete_old_stats_snapshots(self, time: str):
        query = f"""
        SELECT player_id FROM hunters.player_stats_by_player_id"""
        res = self.session.execute(query)
        for row in res:
            for column in row._fields:
                pid = getattr(row, column)

            query = f"""
            DELETE FROM hunters.player_stats_by_player_id_and_time_logs WHERE player_id = {pid} AND time < '{time}'
            """

            res = self.session.execute(query)

    def delete_old_resource_snapshots(self, time: str):
        query = f"""
        SELECT player_id FROM hunters.game_data_by_player_id"""
        res = self.session.execute(query)
        for row in res:
            for column in row._fields:
                pid = getattr(row, column)

            query = f"""
            DELETE FROM hunters.game_data_by_player_id_and_time_logs WHERE player_id = {pid} AND time < '{time}'
            """

            res = self.session.execute(query)
