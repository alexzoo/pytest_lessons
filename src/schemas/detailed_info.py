from typing import List

from pydantic import BaseModel

from src.schemas.owners import Owners
from src.schemas.physical import Physical


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]

