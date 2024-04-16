#3circular reference

#[objA] ---> [objB]
#[objB] ---> [objA]

class Box:
    def __init__(self, number):
        self.number=number
        self.nextBox = None

    def __str__(self) -> str:
        return f"BOX [{self.number:^10}] -> {self.nextBox}"
    
    def __eq__(self, other) -> bool:
        return self.number == other.number

b1=Box(100)
b2=Box(101)
b3=Box(103)

b1.nextBox = b2
b2.nextBox = b3
# print(id(b1), id(b2),id(b3),sep="\n" )
print(id(b2),id(b1.nextBox ),sep="\n" )
# print(b2)

if b2 is b1.nextBox:
    print("Yes")


s1 = "Hello"
s2 = "Hell" + "o"

if s1 == s2:
    print ("Are equal")
if s1 is s2:
    print ("Are identical")


l1 =[1,2]
l2 =[1,2]

if l1 == l2:
    print ("Lists are equal")
if l1 is l2:
    print ("Lists are identical")

t1 =(1,2)
t2 =(1,2)

if t1 == t2:
    print ("tuples are equal")
if t1 is t2:
    print ("tuples are identical")