from pymongo import MongoClient
from bson.objectid import ObjectId
from models.guild import Guild, Member, GuildCreation
from fastapi import HTTPException
from typing import Union


class GuildsService:
    def __init__(self):
        self.client = MongoClient("mongodb", 27017)
        db = self.client["guilds"]
        self.guilds = db['guilds']
        self.members = db['members']

    async def get_guilds(self, limit: int):
        guilds = list(self.guilds.find())[:limit]
        if guilds:
            for doc in guilds:
                doc["_id"] = str(doc["_id"])
        return {"guilds": guilds}

    async def get_members(self, gid: str):
        members = list(self.members.find({"gid": gid}))
        return members

    async def get_guild_by_member(self, player_id: int):
        entry = self.members.find_one({"player_id": player_id})
        if entry:
            guild = self.guilds.find_one({"_id": ObjectId(entry["gid"])})
            guild["_id"] = str(guild["_id"])  # parse hex
            return guild

    async def create_guild(self, guild: GuildCreation):
        result = self.guilds.insert_one(Guild(**guild.dict()).dict())
        if result.acknowledged:
            return str(result.inserted_id)

    async def join_guild(self, member: Member):
        # member_exists = self.members.find_one(member.dict())
        # if member_exists:
        #     return False

        # guild = self.guilds.find_one({"_id": ObjectId(member.gid)})
        # if not guild:
        #     return False

        self.members.insert_one(member.dict())
        self.guilds.update_one({"_id": ObjectId(member.gid)}, {"$inc": {"num_members": 1}})
        return True

    async def leave_guild(self, gid: str, player_id: int):
        self.guilds.update_one({"_id": ObjectId(gid)}, {"$inc": {"num_members": -1}})
        self.members.delete_one({"gid": gid, "player_id": player_id})
        guild = self.guilds.find_one({"_id": ObjectId(gid)})
        # if not guild:
        #     return False
        if guild["num_members"] == 0:
            await self.delete_guild(gid)
        return True

    async def delete_guild(self, gid: str):
        self.guilds.delete_one({"_id": ObjectId(gid)})
        self.members.delete_many({"gid": gid})
        return True
