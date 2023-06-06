from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Union


class Guild(BaseModel):
    name: str
    description: str
    num_members: int
    limit_members: int


class Member(BaseModel):
    gid: Union[str, None]
    player_id: int
    player_name: str


class GuildCreation(BaseModel):
    name: str
    description: str
    num_members: int = 0
    limit_members: int

    player_id: int
    player_name: str


if __name__ == "__main__":
    a = GuildCreation(name="name", description="description", limit_members=20, player_id=1, player_name="name")
    print(a)
    print(Guild(**a.dict()))