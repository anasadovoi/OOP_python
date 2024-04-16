## Address <> Student

class Student:
    def __init__(self,name, age, grade, loc):
        self.name=name
        self.age=age
        self.grade=grade
        self.loc = loc
    def __str__(self):
        return f"STUDENT {self.name} {self.age}{self.grade}\n{self.loc}"
    
########################################
location={
    "country": "Moldova",
    "city"   : "Chisinau"
}

s1 = Student("John", 30, 5, location)
s2 = Student ("Marry", 29, 6, location)

s1.loc["city"] = "Balti"
print(s1)
print(s2)