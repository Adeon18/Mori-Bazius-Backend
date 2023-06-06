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

        @self.app.get("/members")
        async def get_members(gid: str):
            r = await self.service.get_members(gid)
            return str(r)

        @self.app.get("/guild")
        async def get_guild_by_member(player_id: int):
            return await self.service.get_guild_by_member(player_id)

        @self.app.post("/guilds/new")
        async def create_guild(new_guild: GuildCreation):
            gid = await self.service.create_guild(new_guild)
            if gid:
                member = Member(gid=gid, player_id=new_guild.player_id, player_name=new_guild.player_name)
                await self.service.join_guild(member)
                return member

        @self.app.post("/guilds/members/new")
        async def join_guild(member: Member):
            await self.service.join_guild(member)
            return member

        @self.app.delete("/guilds/leave")
        async def leave_guild(gid: str, player_id: int):
            await self.service.leave_guild(gid, player_id)
            return True

        @self.app.delete("/guilds/delete")
        async def delete_guild(gid: str):
            await self.service.delete_guild(gid)
            return gid


controller = GuildsController()


if __name__ == "__main__":
    uvicorn.run(controller.app, host="0.0.0.0", port=6969)
