# train with wagons

class Wagon:
    def __init__(self,number):
        if type(number) ==int and number >0:
            self.number = number
        elif type(number) != int: 
            #HW1: add type error when not int
            raise TypeError("Wagon number not int ")
        else:
            raise ValueError("Incorrect wagon number")
    def __str__(self) -> str:
            return f"[{self.number:^9}]"
    def __repr__(self) -> str:
         return self.__str__()


class Train:
     def __init__(self):
          self.wagons = []

     def addWagon(self, wagon):
        # HW3: Validate the wagon; don't add a wagon with the same number
        if wagon not in self.wagons:
            self.wagons.append(wagon)
        else:
            print(f"Wagon {wagon} already exists. Cannot add duplicate wagons.")


    #HW4:
    # create - removeWagon(self, number)
     def removeWagon(self, number):
          if number in self.wagons:
            self.wagons.remove(number)
          else:
            print(f"Wagon {number} does not exist")
     def __str__(self) :
            #HW2: 
            #1. using for loop 
            #2. join, split
            #3.  built in function python map
            # <TRAIN>[10] =[20]
            return f"<TRAIN>{self.wagons}"
##########################

train = Train()
train.addWagon(Wagon(10))
train.addWagon(Wagon(20))
train.addWagon(Wagon(20))
train.addWagon(Wagon(10))
train.removeWagon(Wagon(10))
print(train)

