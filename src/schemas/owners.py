from pydantic import BaseModel, EmailStr
from pydantic.types import PaymentCardNumber


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr
