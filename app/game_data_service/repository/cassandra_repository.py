import os
from cassandra.cluster import Cluster

from repository.game_data_repository import GameDataRepository

from domain.resources import Resources
from domain.stats import Stats

class CassandraRepository(GameDataRepository):
    def __init__(self) -> None:
        cassandra_endpoint = os.getenv("CASSANDRA_ENDPOINT")
        cassandra_endpoint = cassandra_endpoint if cassandra_endpoint is not None else "localhost"
        cassandra_port = os.getenv("CASSANDRA_PORT")
        cassandra_port = cassandra_port if cassandra_port is not None else 9042

        self.cassandra_client = Cluster([cassandra_endpoint], port=cassandra_port)
        self.session = self.cassandra_client.connect()

    
    def get_stats(self, player_id: int) -> dict:
        query = f"""
        SELECT * FROM hunters.player_stats_by_player_id
        WHERE player_id = {player_id}
        """
        res = self.session.execute(query)
        json = []
        for row in res:
            result = {}
            for column in row._fields:
                result[column] = getattr(row, column)
            json.append(result)
            break


        return json[0] if len(json) > 0 else {}
    
    def get_resources(self, player_id: int) -> dict:
        query = f"""
        SELECT * FROM hunters.game_data_by_player_id
        WHERE player_id = {player_id}
        """
        res = self.session.execute(query)
        json = []
        for row in res:
            result = {}
            for column in row._fields:
                result[column] = getattr(row, column)
            json.append(result)
            break


        return json[0] if len(json) > 0 else {}
    
    def set_stats(self, player_id: int, stats: Stats):
        stats_to_update = dict(((key, value) for key, value in vars(stats).items() if value is not None))
        keys_to_update = list(stats_to_update.keys())
        values_to_update = [stats_to_update[key] for key in keys_to_update]

        if "player_id" not in stats_to_update:
            keys_to_update.insert(0, "player_id")
            values_to_update.insert(0, player_id)

        query = f"""
        INSERT INTO hunters.player_stats_by_player_id 
        ({", ".join(keys_to_update)}) VALUES ({", ".join([str(v) for v in values_to_update])})
        """

        self.session.execute(query)

    def set_resources(self, player_id: int, resources: Resources):
        resources_to_update = dict(((key, value) for key, value in vars(resources).items() if value is not None))
        keys_to_update = list(resources_to_update.keys())
        values_to_update = [resources_to_update[key] for key in keys_to_update]

        if "player_id" not in resources_to_update:
            keys_to_update.insert(0, "player_id")
            values_to_update.insert(0, player_id)

        query = f"""
        INSERT INTO hunters.game_data_by_player_id 
        ({", ".join(keys_to_update)}) VALUES ({", ".join([str(v) for v in values_to_update])})
        """

        self.session.execute(query)