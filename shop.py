from concurrent.futures import ProcessPoolExecutor, Future
from constants import FULL_SHOP
from meat_type import MeatType
from kebab import Kebab
from order import Order
from queue import Queue

class Shop():

    def __init__(self, numberOfSeats: int, numberOfGrills: int):
        self.seats = Queue(numberOfSeats)
        for i in range(0, numberOfSeats): self.seats.put(i)
        self.grills = Queue(numberOfGrills)
        for i in range(0, numberOfGrills): self.grills.put(i)

    def takeSeat(self) -> int:
        if self.seats.empty():
            print(FULL_SHOP)
        return self.seats.get()
        
    def pay(self, seat: int) -> None:
        self.seats.put(seat)

    def takeGrill(self) -> int:
        return self.grills.get()
    
    def releaseGrill(self, grill: int) -> None:
        self.grills.put(grill)
