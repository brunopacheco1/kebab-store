import logging
from concurrent.futures import ProcessPoolExecutor, Future
from constants import NUMBER_OF_CUSTOMERS, NUMBER_OF_GRILLS, NUMBER_OF_SEATS
from shop import Shop
from customer import Customer

logger = logging.getLogger(__name__)

def error_callback(future: Future):
    e = future.exception()
    if e is not None:
        logger.error("Executor Exception", exc_info=e)

with ProcessPoolExecutor() as pool:
    shop = Shop(NUMBER_OF_SEATS, NUMBER_OF_GRILLS)

    for i in range(0, NUMBER_OF_CUSTOMERS):
        customer = Customer()
        future = pool.submit(customer.eatKebab, args=(pool, shop))
        future.add_done_callback(error_callback)

    pool.shutdown(wait=True)
