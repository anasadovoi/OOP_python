from Meme import Meme
from User import User

user1 = User("johny", "j@yahoo.com", "password1")
print(user1)

# object creation
meme_1= Meme("IT Joke", user1, 4.5)
meme_2= Meme("Aerospace", user1, 4.7)

user1.printMemes()

