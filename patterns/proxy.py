
# ########## PROVIDER #############
# [app] <------- proxy ------> [Box]

class Box:
    
    # LIGHTweight proxy
    def __getattr__(self,name):
        print(f"You are trying to access '{name}'")
    def __setattr__(self,name,value):
        print(f"You are trying to set '{name}' = '{value}'")
    # LIGHTweight proxy

# ########## CONSUMER #############
b = Box()
b.value = 100 # write
v = b.value # read the value from the box


# [app] <------- write proxy ------> [Box]
# [app] <------- read proxy ------> [Box]
