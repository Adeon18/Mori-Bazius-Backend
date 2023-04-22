from repository.game_data_repository import GameDataRepository
from repository.cassandra_repository import CassandraRepository

from common.game_data.resources import Resources
from common.game_data.stats import Stats

class GameDataService:
    def __init__(self, repo: GameDataRepository) -> None:
        self.repo = repo
    
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