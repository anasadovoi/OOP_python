from datetime import datetime
from random import randint

class Meme:
    last_id =1
    def __init__(self, title,author, rating):
        self.title = title
        self.author = author
        self.author.memes.append(self)
        self.rating = rating

        self.published = datetime.now()
        #self.id = randint(1,1_000_000_000_000)
        self.id=Meme.last_id
        Meme.last_id +=1
    def __str__(self) -> str:
        return f"Meme: '{self.title}' \n\
                author: '{self.author}'\n\
                rating: '{self.rating}'\n\
                published:'{self.published}'\n\
                id: {self.id}"
    
    def __gt__(self, other):
        return self.rating> other.rating
    