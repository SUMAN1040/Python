name = input("Enter your name:")
print(f"Good Afternoon {name}")



######
letter = '''Dear <|Name|>,
            You are selected! 
            <|Date|>'''

print(letter.replace("<|Name|>", "Suman").replace("<|Date|>", "11/11/2003"))


#####
name = "Suman  Kumar  Dey"
print(name.find("  "))


#####
name = "Suman Kumar  Dey"
print(name.replace("  "," "))

#######
#Strings are immutable which means that we cannot change them by 
# running functions on them


#######
letter = "Dear Suman,\n\tthis python course is nice.\nThanks"

print(letter)