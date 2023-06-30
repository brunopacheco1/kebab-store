from concurrent.futures import ThreadPoolExecutor
from constants import NUMBER_OF_CUSTOMERS, NUMBER_OF_GRILLS, NUMBER_OF_SEATS
from shop import Shop
from customer import Customer

pool = ThreadPoolExecutor(max_workers=2 * NUMBER_OF_CUSTOMERS)
 
shop = Shop(pool, NUMBER_OF_SEATS, NUMBER_OF_GRILLS)

for i in range(0, NUMBER_OF_CUSTOMERS):
    customer = Customer(shop)
    pool.submit(customer.eatKebab)
 
pool.shutdown(wait=True)
