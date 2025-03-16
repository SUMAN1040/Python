#Seven fruits i a list
fruits = []

f1 = input("Enter Fruits name:")
fruits.append(f1)
f2 = input("Enter Fruits name:")
fruits.append(f2)
f3 = input("Enter Fruits name:")
fruits.append(f3)
f4 = input("Enter Fruits name:")
fruits.append(f4)
f5 = input("Enter Fruits name:")
fruits.append(f5)
f6 = input("Enter Fruits name:")
fruits.append(f6)
f7 = input("Enter Fruits name:")
fruits.append(f7)

print(fruits)


'''
# Shortened version using list comprehension
fruits = [input("Enter Fruits name: ") for _ in range(7)]

print(fruits)
'''

#########
student = [int(input("Enter marks here:"))for _ in range(6)]
student.sort()
print(f"List of number in stored in marks:{student}")



##########
a = (34, 234, "Suman")
a[2] = "Kumar"




#######
l = [2, 3, 4, 5]
print(sum(l))

##########
a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)


