from constants import PREPARING_KEBAB, PREPARED_KEBAB, FREE_GRILL
from meat_type import MeatType
from kebab import Kebab
# from shop import Shop - TODO Circular dependency
import time
import itertools
cont = itertools.count()

class Order():

    def __init__(self, shop, meatType: MeatType):
        self.shop = shop
        self.meatType = meatType

    def prepareKebab(self) -> Kebab:
        grill = self.shop.takeGrill()
        print(PREPARING_KEBAB % grill)
        time.sleep(2)
        kebab = Kebab(next(cont), self.meatType, 8.5)
        print(PREPARED_KEBAB % (kebab.id(), self.meatType, grill))
        if (self.shop.releaseGrill(grill)):
            print(FREE_GRILL % grill)
        return kebab
