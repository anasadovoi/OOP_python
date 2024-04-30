current_year = 2021
in_value = input("Enter your b.y.: ")
try:
    birth_year = int(in_value)
    age = current_year - birth_year
    print(f"You're {age} years old")
except:
    print("ERROR, wrong year value!!!!")



# Key moments
# traceback
# line(origin)
# error type


# VM                         ^
# module responsibility ???? ^
# >int(v)           >>>> ValueError
