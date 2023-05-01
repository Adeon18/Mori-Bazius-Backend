from pydantic import BaseModel
from typing import Union
import datetime


class User(BaseModel):
    username: Union[str, None] = None
    password: Union[str, None] = None
    uid: Union[int, None] = None
    created_on: Union[datetime.datetime, None] = None
