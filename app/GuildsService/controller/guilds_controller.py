from service.guilds_service import GuildsService
from models.guild import Guild, Member, GuildCreation

from fastapi import FastAPI
import uvicorn


class GuildsController:
    def __init__(self):
        self.app = FastAPI()
        self.service = GuildsService()

        @self.app.get("/guilds")
        async def get_guilds():
            r = await self.service.get_guilds()
            return str(r)

        @self.app.get("/members/{gid}")
        async def get_guilds(gid: str):
            r = await self.service.get_members(gid)
            return str(r)

        @self.app.post("/guilds/new")
        async def create_guild(new_guild: GuildCreation):
            gid = await self.service.create_guild(new_guild)
            if gid:
                member = Member(gid=gid, player_id=new_guild.player_id, player_name=new_guild.player_name)
                await self.service.join_guild(member)
                return member

        @self.app.post("/guilds/{gid}/members/{player_id}")
        async def join_guild(member: Member):
            await self.service.join_guild(member)
            return member

        @self.app.delete("/guilds/{guild_id}/members/{player_id}")
        async def leave_guild(member: Member):
            await self.service.leave_guild(member)
            return member

        @self.app.delete("/guilds/{guild_id}/")
        async def delete_guild(guild_id: str):
            await self.service.delete_guild(guild_id)
            return guild_id



controller = GuildsController()


if __name__ == "__main__":
    uvicorn.run(controller.app, host="0.0.0.0", port=6969)
