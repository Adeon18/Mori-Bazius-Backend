from pydantic import BaseModel
from typing import Union
import datetime


class User(BaseModel):
    username: str
    password: str
    uid: Union[int, None] = None
    created_on: Union[datetime.datetime, None] = None
