# OOP Object Oriented Programming

#keypoints:
#   - many langs: py, java, js, php, c++, c#, ...
#   - higher level (Abstraction, Inheritance, Polymorphism, Behaviour)
#   - no choice


#type()
# b = True
# i = 10
# f = 0.5
# s = "abc"
# l=[1,2,3]
# d = {"a":1, "b":2}

# def fun():
#     pass

#  ###############################
# print(type(b))
# print(type(i))
# print(type(s))
# print(type(f))
# print(type(s))
# print(type(l))
# print(type(d))
# print(type(fun))


# class and object(structure and behavior)
#PascalCaseClassName

# Class 2 points of view:
#   1.Box (properties/methods())
#   2. Factory -> create  -> objects   

# Object - a copy of the class, no identical obj exist 
# class Human: # create a new data type
#     pass

# print(type(Human))
# # create objects of type Human
# h1 = Human()
# h1.name = "John"
# h1.age = 24
# h2 = Human()
# h1.name = "Marry"
# h1.age = 34
# print(h1.name, h1.age)
# print(h2.name, h2.age)


# 4 independent boxes

# h1_name
# h1_age
# h2_name
# h2_age

# 2 independent boxes

#h1
#   .name
#   .age

#h2
#   .name
#   .age



############################################
#       Object binding/self
############################################

#   mine
#   this + context
# -----------------------------------------

# ----------- room ---------------
#|                                |
#|                                |
#|            chair1              |
#|            chair2              |
#|            chair3              |
#|                                |
#|                                |
# ----------- room ---------------

# Real world: Take a sit on this chair. (Which one?)

# Python: self
#   self -context
# If inside a class you define a function with self as a parameter, it will be automatically attached to each object

class Human: # create a new data type
    def hi(self):
        print("Hi! I am a person ")
    def bye(self):
        print("Bye!!!")


h1 = Human()
h2 = Human()

h1.hi()
h2.hi()
h1.bye()
h2.bye()

