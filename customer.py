from meat_type import MeatType
from constants import FREE_SEAT, START_EAT_KEBAB, FINISH_EAT_KEBAB
from shop import Shop
import time

class Customer:

    def __init__(self, shop: Shop):
        self.shop = shop

    def eatKebab(self):
        seat = self.shop.takeSeat()
        kebab = self.shop.order(MeatType.random()).result()
        print(START_EAT_KEBAB % (seat, kebab.id))
        time.sleep(1)
        print(FINISH_EAT_KEBAB % (seat, kebab.id))
        self.shop.pay(seat)
        print(FREE_SEAT % seat)
