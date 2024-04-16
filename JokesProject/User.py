from datetime import datetime
from Model import Model

class User(Model):

    def __init__(self,name,email,password):
        super().__init__()
        self.name = name
        self.email = email
        self.password = password
        self.created = datetime.now()
        self.memes=[]

    def __str__(self) -> str:
        return f"User: {self.name} ({self.email})"
    
    def printMemes(self):
        for meme in self.memes:
            print(meme)
