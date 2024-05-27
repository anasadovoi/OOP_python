from Meme import Meme
from User import User
from Storage import Storage

# user = User("John", "j@yahoo.com", 'password1')
# meme1= Meme("Title123", user, 4.5)
# #user.setName("FNBEHX")
# print(user.getName())


# # object creation
#post_1= Meme("IT Joke", user1, 4.5)
#post_2= Meme("Aerospace", user1, 4.7)

#create the Storage obj
# fileStorage1 = Storage.openStorage()
# fileStorage2 = Storage.openStorage()
# fileStorage3 = Storage.openStorage()
# fileStorage3.save(user)
# Storage.closeStorage()

#print(user.toJSON())

# json =    """   {
#                   "name":"John",
#                   "email":"j@yahoo.com",
#                   "password":"password1"
#                  }

# """
# user = User.fromJson(json)
# print(user)

storage = Storage.open()

user = storage.load()
print(user)

Storage.close()