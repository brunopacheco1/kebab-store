from constants import PREPARING_KEBAB, PREPARED_KEBAB, FREE_GRILL
from meat_type import MeatType
from kebab import Kebab
# from shop import Shop - TODO Circular dependency
import time
import itertools
counter = itertools.count()

class Order():

    def prepareKebab(self, shop, meatType: MeatType) -> Kebab:
        grill = shop.takeGrill()
        print(PREPARING_KEBAB % grill)
        time.sleep(2)
        kebab = Kebab(next(counter), meatType, 8.5)
        print(PREPARED_KEBAB % (kebab.id, kebab.meatType, grill))
        shop.releaseGrill(grill)
        print(FREE_GRILL % grill)
        return kebab
