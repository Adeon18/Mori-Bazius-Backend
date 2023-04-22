from pydantic import BaseModel

class Stats(BaseModel):
    player_id: int | None = None
    level: int | None = None
    power: int | None = None
    exp: int | None = None
    hunters: int | None = None
    masters: int | None = None
