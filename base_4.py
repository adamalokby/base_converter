def get_number():
    """
    This function takes no arguments, and is 
    designed to fetch the number that the user
    would like to convert into a different base.
    """
    return int(input("Choose a number to find it's base counterpart.\n"))

def get_base():
    """
    This function takes no arguments, and is 
    designed to fetch the base that the user
    would like to convert into their number into.
    """
    return int(input("Which base is the number system?\n"))

number = get_number()
base = get_base()

y = int(x / base)

a = int(x%base)

z = int(y/base)

b = int(y%base)

l = int(z/base)

c = int(z%base)

m = int(l/base)

d = int(l%base)

print (d , c , b , a)
