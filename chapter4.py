#list and tuple
friends = ["oranges", "Apples", "banana", "Suman", 5, 23.72, False]
print(friends[0])

friends[0] = "Kumar" #unlike Strings lists are mutable

print(friends[0])

print(friends[1:4])  #slicing 


##################################
friends.append("Harry")
print(friends)

friends.insert(1, "Suman")
print(friends)


l1 = [1, 5, 3, 4, 4]
l1.sort()
print(l1)

l1.reverse()
print(l1)


l1.insert(2, "Suman") # Insert Suman such that its index in the list is 2
print(l1)

l1.pop(1) # remove the element at index 1
print(l1)


l1.remove("Suman")
print(l1)




''' Python List Methods
# Creating a sample list
lst = [3, 1, 4, 1, 5, 9, 2]

# 1. Adding Elements
lst.append(6)        # [3, 1, 4, 1, 5, 9, 2, 6]
lst.extend([7, 8])   # [3, 1, 4, 1, 5, 9, 2, 6, 7, 8]
lst.insert(2, 10)    # [3, 1, 10, 4, 1, 5, 9, 2, 6, 7, 8]

# 2. Removing Elements
lst.remove(1)        # Removes first occurrence of 1
lst.pop(3)           # Removes element at index 3
lst.clear()          # Clears the list

# 3. Searching & Counting
lst = [1, 2, 3, 4, 2, 2]
print(lst.index(2))  # 1 (first occurrence)
print(lst.count(2))  # 3

# 4. Sorting & Reversing
lst = [5, 2, 9, 1]
lst.sort()           # [1, 2, 5, 9]
lst.sort(reverse=True)  # [9, 5, 2, 1]
lst.reverse()        # [1, 2, 5, 9]

# 5. Copying
new_lst = lst.copy()

#https://chatgpt.com/share/67d66f47-c9b4-8012-a79d-e8b8ecc0ead0
'''

#Tuple in python
a = (1, 2, 3, 4, 5)
#a[0] = 345  # Tuple can't changed
print(a)
print(type(a))

number = a.count(45)
print(number)
print(a.count(3))



'''
# Creating a tuple
my_tuple = (1, 2, 3, "hello", 3.14)

# Accessing elements
print(my_tuple[0])    # 1
print(my_tuple[-1])   # 3.14

# Tuple slicing
print(my_tuple[1:4])  # (2, 3, 'hello')

# Tuple operations
new_tuple = my_tuple + (4, 5)  # Concatenation
print(new_tuple)  # (1, 2, 3, 'hello', 3.14, 4, 5)

# Membership check
print(3 in my_tuple)  # True

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # 1 2 3 hello 3.14

# Tuple functions
print(len(my_tuple))        # 5
print(my_tuple.count(3))    # 1
print(my_tuple.index("hello"))  # 3

# Convert tuple to list and back
my_list = list(my_tuple)
my_list.append("new")
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 'hello', 3.14, 'new')
'''


