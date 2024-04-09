from datetime import datetime
from random import randint


class Meme:
    last_id =1
    def __init__(self, title,author, rating):
        self.title = title
        self.author = author
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
    
# object creation
meme_1= Meme("IT Joke", "johnny", 4.5)
meme_2= Meme("Aerospace", "mary", 4.7)

if meme_1 > meme_2:
    print(meme_1)
    print(meme_2)
else:
    print(meme_2)
    print(meme_1)