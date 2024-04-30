class Wagon:
    def __init__(self, number):
        if isinstance(number, int) and number > 0:
            self.number = number
        elif not isinstance(number, int):
            # HW1: add type error when not int
            raise TypeError("Wagon number must be an integer")
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
            print(f"Wagon {wagon} already exists")

    def removeWagon(self, number):
        for wagon in self.wagons:
            if wagon.number == number:
                self.wagons.remove(wagon)
                print(f"Removed wagon {wagon}")
                return
        print(f"Wagon {number} not found in the train")

    def __str__(self) -> str:
        return ", ".join(map(str, self.wagons))


train = Train()
train.addWagon(Wagon(10))
train.addWagon(Wagon(70))
train.addWagon(Wagon(20))
print("Train wagons:", train)

train.removeWagon(20)
print("Train wagons:", train)
