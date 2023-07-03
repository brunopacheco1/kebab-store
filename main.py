import logging
from multiprocessing import Pool, Manager, Lock, Value
from constants import *
from shop import Shop
from meat_type import MeatType
from kebab import Kebab
import time
import itertools

logger = logging.getLogger(__name__)

def error_callback(error):
    logger.error("Executor Exception", exc_info=error)

def order(shop: Shop, counter):
    seat = shop.takeSeat()
    kebab = prepareKebab(shop, MeatType.random(), counter)
    eatKebab(seat, kebab)
    shop.pay(seat)
    print(FREE_SEAT % seat)

def prepareKebab(shop, meatType: MeatType, counter) -> Kebab:
    grill = shop.takeGrill()
    print(PREPARING_KEBAB % grill)
    time.sleep(2)
    kebab = Kebab(counter.value, meatType, 8.5)
    counter.value += 1
    print(PREPARED_KEBAB % (kebab.id, kebab.meatType, grill))
    shop.releaseGrill(grill)
    print(FREE_GRILL % grill)
    return kebab

def eatKebab(seat: int, kebab: Kebab):
    print(START_EAT_KEBAB % (seat, kebab.id))
    time.sleep(1)
    print(FINISH_EAT_KEBAB % (seat, kebab.id))

with Pool(processes=NUMBER_OF_CUSTOMERS) as pool:
    manager = Manager()
    counter = manager.Value('i', 0)
    counter.value = 0
    shop = Shop(manager, NUMBER_OF_SEATS, NUMBER_OF_GRILLS)

    for i in range(0, NUMBER_OF_CUSTOMERS):
        pool.apply_async(order, [shop, counter], error_callback=error_callback)

    pool.close()
    pool.join()
