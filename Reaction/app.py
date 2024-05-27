class Reaction:

    allowed = ["haha", "like", "dislike", "angry"]

    def __init__(self,type):
        if type in Reaction.allowed:
            self.__type = type
        else:
            raise ValueError(f"The reaction '{type}' is not allowed")
        
    def getType(self):
         return self.__type
        
    def __str__(self):
            return f"REACTION: {self.__type}"
    
    def fromTxtFile():
         file = open("reaction.txt", "r")
         data = file.read() # <---- "haha"
         file.close()

         reaction = Reaction(data)
         return reaction
    
    def toTxtFile(reaction):
         file = open("reaction.txt", "w")
         file.write(reaction.getType()) # <---- "haha"
         file.close()
################################
# 3 x reactions: haha, haha, like

# react_1 = Reaction("haha")
# react_2 = Reaction("haha")
# react_3 = Reaction("like")

# print(react_1)
# print(react_2)
# print(react_3)

# react_1 = Reaction.fromTxtFile()
react_1 =Reaction("like")
Reaction.toTxtFile(react_1)

print(react_1)