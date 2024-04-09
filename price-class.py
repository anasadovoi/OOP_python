class Money:
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
    def __str__(self):
        return "["+str(self.value)+self.currency+"]"
    def __sub__(self, m):
        return Money(self.value - m.value, self.currency)
##########################################
        
jun_salary = Money(1000, "EUR")
travel_cost = Money(789, "EUR")
rest        = jun_salary - travel_cost

# 1) show the values on the screen

print(jun_salary)
print(travel_cost)
print (rest)