from pydantic import BaseModel

class Stats(BaseModel):
    player_id: int | None = None
    level: int | None = None
    power: int | None = None
    wins: int | None = None
    loses: int | None = None
    win_rate_percent: int | None = None
    total_upgr: int | None = None
    upgr_0: int | None = None
    upgr_1: int | None = None
    upgr_2: int | None = None
    upgr_3: int | None = None
