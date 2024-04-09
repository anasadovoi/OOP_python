# class | type definition
class Meme:
    def __init__(self, title,author, rating):
        self.title = title
        self.author = author
        self.rating = rating
    def __str__(self) -> str:
        return f"Meme: {self.title}"
    
    

# object creation
meme_1= Meme("IT Joke", "johnny", 4.5)
meme_2= Meme("Aerospace", "mary", 4.7)

print(meme_1)
print(meme_2)
