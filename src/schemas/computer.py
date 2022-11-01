from pydantic import BaseModel

from src.enums.user_enums import Statuses
from pydantic.types import PastDate, FutureDate
from pydantic.networks import IPv4Address, IPv6Address

from src.schemas.detailed_info import DetailedInfo


class Computer(BaseModel):
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo

