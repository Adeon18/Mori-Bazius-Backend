from fastapi import FastAPI
from service.gateway_service import GatewayService
from common.game_data.stats import Stats
from common.game_data.resources import Resources
from common.game_data.user import User
from common.game_data.guild import GuildCreation, Member


class App:
    def __init__(self):
        self.app = FastAPI()
        self.service = GatewayService()

        # HANGLING REGISTRATION VALIDATION ETC
        @self.app.post("/register")
        async def game_register_post(user_data: User):
            return self.service.handle_register_operation(user_data)

        @self.app.post("/login")
        async def game_login_post(user_data: User):
            return self.service.handle_login_operation(user_data)

        # HANDLING GAME DATA
        @self.app.get("/game_data/stats")
        async def game_data_stats(player_id: int):
            return self.service.get_game_stats(player_id)

        @self.app.post("/game_data/stats")
        async def game_data_set_stats(player_id: int, stats: Stats):
            return self.service.set_game_stats(player_id, stats)

        @self.app.get("/game_data/resources")
        async def game_data_resources(player_id: int):
            return self.service.get_game_resources(player_id)

        @self.app.post("/game_data/resources")
        async def game_data_set_resources(player_id: int, resources: Resources):
            return self.service.set_game_resources(player_id, resources)

        @self.app.get("/game_data/leaderboard")
        async def game_data_leaderboard(limit: int):
            return self.service.get_game_leaderboard(limit)
        
        @self.app.get("/game_data/average")
        async def game_data_average(player_id: int):
            return self.service.get_game_data_average(player_id)

        # HANDLING GUILDS
        @self.app.get("/guilds")
        async def get_guilds():
            return self.service.get_guilds()

        @self.app.get("/members")
        async def get_members(gid: str):
            return self.service.get_members(gid)

        @self.app.get("/guild")
        async def get_guild_by_member(player_id: int):
            return self.service.get_guild_by_member(player_id)

        @self.app.post("/guilds/new")
        async def create_guild(new_guild: GuildCreation):
            print(new_guild)
            return self.service.create_guild(dict(new_guild))

        @self.app.post("/guilds/members/new")
        async def join_guild(member: Member):
            return self.service.join_guild(member)

        @self.app.delete("/guilds/leave")
        async def leave_guild(gid: str, player_id: int):
            return self.service.leave_guild(gid, player_id)

        @self.app.delete("/guilds/delete")
        async def delete_guild(gid: str):
            return self.service.delete_guild(gid)
