from datetime import datetime
from random import randint
from Model import Model

class Meme(Model):
    def __init__(self, title,author, rating):
        # initialization of Model specific values
        super().__init__()
        # initialization of Model specific values
        self.title = title
        self.author = author
        self.author.memes.append(self)
        self.rating = rating

        self.published = datetime.now()
        #self.id = randint(1,1_000_000_000_000)

    def __str__(self) -> str:
        return f"Meme({self.id}): '{self.title}' \n\
                author: '{self.author}'\n\
                rating: '{self.rating}'\n\
                published:'{self.published}'"
    
    def __gt__(self, other):
        return self.rating> other.rating
    