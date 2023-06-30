from concurrent.futures import ThreadPoolExecutor, Future
from constants import FULL_SHOP
from meat_type import MeatType
from kebab import Kebab
from order import Order
from queue import Queue

class Shop():

    def __init__(self, pool: ThreadPoolExecutor, numberOfSeats: int, numberOfGrills: int):
        self.pool = pool
        self.seats = Queue(numberOfSeats)
        for i in range(0, numberOfSeats): self.seats.put(i)
        self.grills = Queue(numberOfGrills)
        for i in range(0, numberOfGrills): self.grills.put(i)
            
        self.numberOfGrills = numberOfGrills

    def takeSeat(self) -> int:
        if self.seats.empty():
            print(FULL_SHOP)
        return self.seats.get()
    
    def order(self, meatType: MeatType) -> Future[Kebab]:
        order = Order(self, meatType)
        return self.pool.submit(order.prepareKebab)
    
    def pay(self, seat: int):
        self.seats.put(seat)

    def takeGrill(self) -> int:
        return self.grills.get()
    
    def releaseGrill(self, grill: int):
        self.grills.put(grill)
