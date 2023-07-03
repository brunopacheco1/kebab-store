from multiprocessing import Manager
from constants import FULL_SHOP

class Shop():

    def __init__(self, manager: Manager, numberOfSeats: int, numberOfGrills: int):
        self.seats = manager.Queue(numberOfSeats)
        for i in range(0, numberOfSeats): self.seats.put(i)
        self.grills = manager.Queue(numberOfGrills)
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
