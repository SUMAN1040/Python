# Variables and data Types

a = 1
b = 2
print(a+b)

#Ram : Random Access Memory
# Variables are stored in RAM
# Variables are stored in memory location

c = 7

name = "Suman"

print (name)

d = 31.37
print(d)


a = 1 #a is an integer
b = 2.34 #b is float
c = "Suman" #c is string
d = False #d is a boolean variable
e = None # e is a none type variable


#####################################################################

aaaa = 34

Suman = 24

Kumar = 34

_Suman = 23

#  @suman = 34  invalid due to @symbol
#  2suman = 34  invalid due to starting with number

#######################################################

#Arithmetic Operator

a  = 30
b = 2
c = a + b
print(c)


#Assignment operator
a = 4-2
b = 6
# b += 3 
b *= 3

print(a, b)


# Comparison Operators
d = 5<4
ce = 4>1
print(d, ce)

cds = 3==4
print(cds)


#Logical Operators

e = True or False
print(e)

# Truth table of "or"
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not(True))


#Type Casting

a = "31.4"
b = float(a)
t = type(b)

print(t)

print(int(float("24.12")))

#Input Functions

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))

print("Number a is:", a)
print("Number a is:", b)
print("Sum is :", a + b)