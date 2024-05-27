from datetime import datetime
from Model import Model
from json import loads

class User(Model):

    def __init__(self,name,email,password):
        self.setName(name)
        super().__init__()
        #HW1: don't allow spaces ' '
        if type(name) == str:
            if len(name) >= 2:
                self.__name = name
            else:
                raise ValueError("name must have at least 2 characters length")
        else:
            raise TypeError("name must be a string")
        # #HW2 apply encapsulation over email:
        #                                 not empty
        #                                 validate format @
        #                                 regular expressions
        self.email = email
        self.password = password
        self.created = datetime.now()
        self.memes=[]

    def setName (self, name):
        if type(name) == str:
            if len(name) >= 2:
                self.__name = name
            else:
                raise ValueError("name must have at least 2 characters length")
        else:
            raise TypeError("name must be a string")
    def getName(self):
        return self.__name
    
    def fromJson(json):
        data = loads(json)
        user = User(data["name"], data["email"], data["password"])
        return user
    
    def toJSON(self):
        memes = "["
        for meme in self.memes:
            memes += f"\"{meme.title}\","
        memes = "]"
        return f""" {{
        "name":"{self.__name}",
        "email":"{self.email}",
        "password":"{self.password}",
        "created":"{self.created}",
        "memes":"{self.memes}"
           }}
        """


    def __str__(self) -> str:
        return f"User: {self.__name} ({self.email})"

    
    def printMemes(self):
        for meme in self.memes:
            print(meme)
