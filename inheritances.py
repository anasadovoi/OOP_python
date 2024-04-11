# INHERITANCE in python >> OOP/Classes
# * hierarchy
# * DRY
# * extending


#BASE CLASS (super class) --> DERIVED CLASSES

#         [Animal]   (+eat)  super ------- generic
#      /           \
#     /             \
#    /               \
#   v                 v
#  [Cat] (eat, +meow)  [Dog] (eat, +bark)------- specific

class Animal:
    def eat(self):
        print("This animal is eating")

class Cat(Animal):
    def meow(self):
        print("Meowwwwwwww!")
class Dog(Animal):
    def bark(self):
        print("Whoffwhoff!")

################################
# some_animal = Animal()
some_cat = Cat()
some_dog = Dog()

# some_animal.eat()
some_cat.eat()
some_dog.eat()
