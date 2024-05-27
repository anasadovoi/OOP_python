from User import User

class Storage:

    storage = None
    
    def open():
        if Storage.storage == None:
            Storage.storage = Storage()
            Storage.storage.file = open ('user.json', 'r')
            return Storage.storage

    # def __init__(self):
    #     self.file = open("data.txt", "r")
        
    def save(self, user):
         self.file.write(user.name)
         #self.file.close()
    
    def load(self):
        json = self.file.read()
        return User.fromJson(json)    
    
    def close():
        Storage.storage.file.close()

    # # destructor
    # def __del__(self):
    #     pass
        