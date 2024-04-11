from datetime import datetime
class User:

    last_id = 1

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        self.created = datetime.now()

        self.memes=[]


        self.id = User.last_id
        User.last_id +=1

    def __str__(self) -> str:
        return f"User: {self.name} ({self.email})"
    
    def printMemes(self):
        for meme in self.memes:
            print(meme)
