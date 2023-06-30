from enum import Enum
from random import choice

class MeatType(Enum):
    CHICKEN = 1
    PORC = 2
    BEEF = 3

    @classmethod
    def random(self):
        return choice(MeatType._member_names_)
