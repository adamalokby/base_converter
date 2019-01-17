x  = int(input("Choose a number to find it's base counterpart.\n"))

base = int(input("Which base is the number system?\n"))


y = int(x / base)

a = int(x%base)

z = int(y/base)

b = int(y%base)

l = int(z/base)

c = int(z%base)

m = int(l/base)

d = int(l%base)

print (d , c , b , a)
