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
        for existing_wagon in self.wagons:
            if existing_wagon.number == wagon.number:
                print(f"Wagon {wagon} already exists")
        self.wagons.append(wagon)

    #HW4:
    # create - removeWagon(self, number)
    def removeWagon(self, number):
        for wagon in self.wagons:
            if wagon.number == number:
                self.wagons.remove(wagon)
    def __str__(self) : 
        # HW2: Display the train wagons using a for loop
        return f"<TRAIN>{' '.join([str(wagon)+'=' for wagon in self.wagons])}"
##########################

train = Train()
train.addWagon(Wagon(10))
train.addWagon(Wagon(70))
train.addWagon(Wagon(20))
train.addWagon(Wagon(20))
print(train)
train.removeWagon(20)
print(train)

