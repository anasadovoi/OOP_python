# classes > __method__()

# METEO DATA

#   1) simple solution
# temp_yesterday = -5.0
# temp_today     = -3.0

# if temp_yesterday < temp_today:
#     print("It's getting warmer")
# elif temp_today == temp_yesterday:
#     print("It's the same")
# else:
#     print("It's getting colder")

# 2) more complex version
    
class Meteo:
    def __init__(self, temp, wind):
        self.temp = temp
        self.wind = wind
    def __lt__(self, m):
        return self.temp < m.temp
    def __eq__(self, m):
        return self.temp == m.temp
         
            
m_yesterday = Meteo(-5.0, 25.00)
m_today     = Meteo(-5.0, 15.00)

if m_yesterday < m_today:
    print("It's getting warmer")
elif m_today == m_yesterday :
    print("It's the same")
else:
    print("It's getting colder")


# REVERSE ENGINEERING
    
#a+b

# 1. type of a?
# 2. type of b?
# 3. looks for that operation in class A