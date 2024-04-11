# create a data containter
#       -wind data(speed direction)

class WindData:
    # fabricates/creates objects
    def __init__(self, speed, direction): #m/s, N/E/S/W/NE/SW
        #if/else
        self.speed = speed
        self.direction=direction
        self.units = "m/s"
    
    def __str__(self) -> str:
        return f"Wind speed: {self.speed} {self.units}\nDirection: {self.direction}"
    
    def __len__(self):
        return self.speed
##################################
wind_sunday = WindData(100, "N")
wind_monday = WindData(10,"S")   

print(wind_monday)
print(wind_sunday)
print(len(wind_monday))
print(len(wind_sunday))
