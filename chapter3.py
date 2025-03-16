name = "Suman"
nameshort = name[0:3]  #Start from index 0 all the way till 3(Excluding 3)
print(nameshort)
character1 = name[1] 
print(character1)



#negative slicing
name = "Suman"
print(name[0:3])
print(name[-4:-1])
print(name[1:4])
print(name[:])
print(name[:4])
print(name[1:])


#Skipping characters
word = "amazing"
print(word[1:6:2])

suman = "kumardey"
print(suman[1:4:2])

alu = "supervision"
print(alu[1:7:1])

#Functions
#len functions
name = "suman"
print(len(name))
print(name.endswith("Su"))
print(name.startswith("ku"))
print(name.capitalize())


#https://chatgpt.com/share/67d6501c-60f4-8012-9c4a-3ca5ccf19b98


print(name.lower())
print(name.upper())
print(len(name))
print(name.title())
print(name.capitalize())
print(name.strip())
print(name.lstrip())
print(name.rstrip())

#Searching and replacing
name2 = "Suman Kumar Dey"
print(name2.find("Suman"))
print(name2.index("Kumar"))
print(name2.rfind("Dey"))
print(name2.replace("Suman", "InnoXcell"))
print(name2.count("a"))


#String splitting and joining
new = "Apple , banana, pineapple"
print(new.split(","))
print(new.rsplit(",", 1))
print("Suman\nKumar\nDey".splitlines())
print("-".join(["Suman", "Kumar", "Dey"]))


#String Formatting 
name_3 = "Suman"
age = 26
print("My name is {} and i am {} year old.".format(name_3, age))
print(f"My name is {name_3} and i am {age} old.")
print("21".zfill(5))
print("Suman".center(10, "-"))
print("Suman".ljust(10, "-"))
print("Suman".rjust(10, "-"))


#Checking String Property
s = "KOtlin"
print(s.startswith("ko"))
print(s.endswith("Sumn"))
print("n".isdigit())
print("Hello".isalpha())   
print("Hello123".isalnum()) 
print("   ".isspace())      
print("hello".islower())    
print("HELLO".isupper())  


#Scape Sequences

a = "Hello Everyone\nI am Suman Kumar Dey\\\"I am a Engineering student\""
print(a)