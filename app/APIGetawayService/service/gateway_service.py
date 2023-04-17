from domain.stats import Stats
from domain.resources import Resources


class GatewayService:
    def __init__(self):
        pass

    def get_game_resources(self, player_id: int):
        # Verify the sender
        # get gata from game_data
        return {"player_id": player_id}

    def set_game_resources(self, player_id: int, resources: Resources):
        # Verify the sender
        # set gata in game_data
        return {"player_id": player_id, "resources": resources}

    def get_game_stats(self, player_id: int):
        # Verify the sender
        # get gata from game_data
        return {"player_id": player_id}

    def set_game_stats(self, player_id: int, stats: Stats):
        # Verify the sender
        # set gata in game_data
        return {"player_id": player_id, "stats": stats}
