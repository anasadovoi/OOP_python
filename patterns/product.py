#Module defines the class

#Factory method
from time import sleep
# loose coupling

class _Food:   #this is a private class
    def __init__(self, name, price):
        self.name=name
        self.price= price

    def __str__(self) -> str:
        return f"[Food] < {self.name:15}:{self.price:7.2f}>"
class _Drink:   #this is a private class
    def __init__(self, name, price):
        self.name=name
        self.price= price

    def __str__(self) -> str:
        return f"[Drink] < {self.name:15}:{self.price:7.2f}>"
    
# factory function
def createProduct(type,name,price):
    sleep(5)
    if type == "food":
        return _Food(name,price)
    elif type == "drink":
        return _Drink(name,price)
    else:
        raise TypeError("only 'food' and 'drink'products can be fabricated")