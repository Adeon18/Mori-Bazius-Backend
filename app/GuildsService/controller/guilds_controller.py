from service.guilds_service import GuildsService
from models.guild import Guild, Member, GuildCreation

from fastapi import FastAPI
import uvicorn


class GuildsController:
    def __init__(self):
        self.app = FastAPI()
        self.service = GuildsService()

        @self.app.get("/guilds")
        def get_guilds():
            r = self.service.get_guilds()
            print(r)
            return str(r)

        @self.app.get("/members/{gid}")
        def get_guilds(gid: str):
            r = self.service.get_members(gid)
            print(r)
            return str(r)

        @self.app.post("/guilds/new")
        def create_guild(new_guild: GuildCreation):
            gid = self.service.create_guild(new_guild)
            print(gid)
            if gid:
                member = Member(gid=gid, player_id=new_guild.player_id, player_name=new_guild.player_name)
                self.service.join_guild(member)

        @self.app.post("/guilds/{gid}/members/{player_id}")
        def join_guild(member: Member):
            self.service.join_guild(member)

        @self.app.delete("/guilds/{guild_id}/members/{player_id}")
        def leave_guild(member: Member):
            self.service.leave_guild(member)

        @self.app.delete("/guilds/{guild_id}/")
        def delete_guild(guild_id: str):
            self.service.delete_guild(guild_id)



controller = GuildsController()


if __name__ == "__main__":
    uvicorn.run(controller.app, host="0.0.0.0", port=6969)
