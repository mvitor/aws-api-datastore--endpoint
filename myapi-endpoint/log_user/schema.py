from ast import Str
from datetime import datetime
from typing import List, Optional
from uuid import uuid4
from pydantic import BaseModel

def user_uid():
    return "USR" + str(uuid4().hex).upper()

class User(BaseModel):
    id: int
    uid: str = user_uid()
    name: str
    signup_ts: datetime = datetime.utcnow
    friends: List[int] = []