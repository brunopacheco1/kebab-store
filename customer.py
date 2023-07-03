from meat_type import MeatType
from concurrent.futures import ProcessPoolExecutor, Future
from constants import FREE_SEAT, START_EAT_KEBAB, FINISH_EAT_KEBAB
from shop import Shop
from order import Order
from kebab import Kebab
import time

class Customer:

    def eatKebab(self, pool: ProcessPoolExecutor, shop: Shop) -> bool:
        seat = shop.takeSeat()
        order = Order()
        futureKebab: Future[Kebab] = pool.submit(order.prepareKebab, args=(shop, MeatType.random()))
        kebab = futureKebab.result()
        print(START_EAT_KEBAB % (seat, kebab.id))
        time.sleep(1)
        print(FINISH_EAT_KEBAB % (seat, kebab.id))
        shop.pay(seat)
        print(FREE_SEAT % seat)
        return True
