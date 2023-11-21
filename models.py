from pydantic import BaseModel


class TarotCard(BaseModel):
    name: str
    description: str
    number: int
    is_birth_card: bool = False
