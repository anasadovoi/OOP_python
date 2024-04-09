# class
# likes + dislikes ^_

class Rating:
    def __init__(self, thumbsUp, thumbsDown) :
        self.thumbsUp = thumbsUp
        self.thumbsDown = thumbsDown
    def __str__(self) :
        return "Rating: 👍"+str(self.thumbsUp)+" 👎"+str(self.thumbsDown)
    def __gt__(self,m):
       return (self.thumbsUp -self.thumbsDown)> (m.thumbsUp - m.thumbsDown)
    def __lt__(self,m):
       return (self.thumbsUp -self.thumbsDown)< (m.thumbsUp - m.thumbsDown)
    def __eq__(self,m):
       return (self.thumbsUp -self.thumbsDown)== (m.thumbsUp - m.thumbsDown)
    def __add__ (self, m):
        return Rating(self.thumbsUp + m.thumbsUp, self.thumbsDown + m.thumbsDown)
    def __sub__ (self, m):
        return Rating(self.thumbsUp - m.thumbsUp, self.thumbsDown - m.thumbsDown)
    #HW1:
    # __lt__, __eq__, __add__, __sub__

###############################################
        
video1_rating = Rating(1000, 10)
video2_rating = Rating(1000, 10)

if video1_rating > video2_rating:
    print("First video is better")
elif video1_rating == video2_rating:
    print("Same rating ")
else:
    print("Second video is better")


print(video1_rating)
print(video2_rating)

#Sum
sum= video1_rating + video2_rating
print(sum)

