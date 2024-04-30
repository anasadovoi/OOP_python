from Meme import Meme
from User import User

user1 = User("John", "j@yahoo.com", 'password1')
user1.setName("FNBEHX")
print(user1.getName())


# # object creation
#post_1= Meme("IT Joke", user1, 4.5)
#post_2= Meme("Aerospace", user1, 4.7)

user1.printMemes()



