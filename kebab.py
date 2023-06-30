from dataclasses import dataclass
from meat_type import MeatType

@dataclass(frozen=True)
class Kebab:
    id: int
    meatType: MeatType
    price: float
