#lecture 0 CS-50 print,functions

# first code

# print("Hello \"World!\" ")    # \"to use quotation in print \" ::: '\' is escap character



"""
name is variable and input prints and take input and stores
in the name variaable
"""
name = input("what's your name?").strip().title()
# strip also have: lstrip, rstrip; to strip in between we use diffrent approach

# Remove white sapces
# name = name.strip()

# Capitalize the string in grametical way not gonna capitalize all character
# name= name.capitalize()

'''
or chain these str functions

name = name.strip().title()
or
name = input("what's your name?").strip().title()
'''

# says hello to enterd named user 
# this is fractional string we given to the print it detacts and take actions accordingly
print(f"hello, {name}")


'''
many other way to print

print("hello,", name)
print("hello,"+ name)
print("hello, "+ name)
print("hello,", name, sep=" ")

print("hello,", end=" ")
print(name)

'''


print("welcome to CS-50 Python", end="\n\n\n")


print("now let's learn more")

first,  last = name.split(" ")
print(f"hello, {first}")