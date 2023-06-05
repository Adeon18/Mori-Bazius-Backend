from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Union


class Guild(BaseModel):
    gid: Union[str, None]
    name: str
    description: str
    num_members: int
    limit_members: int


class Member(BaseModel):
    gid: str
    player_id: int
    player_name: str


class GuildCreation(BaseModel):
    name: str
    description: str
    num_members: int = 0
    limit_members: int

    player_id: int
    player_name: str
