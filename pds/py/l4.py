#Lecture 2 CS-50: loops
'''
i=3
while i!=0:
    print('meow')
    i-=1

print()

for i in [0,1,2]:
     print('meow')

print()

for _ in range(5):
     print('meow')

print()

print("meow\n" * 3,end="")

print()

while True:
     n = int(input("enter n"))
     if n>0:
          break

for _ in range(n):
     print('meow')

'''

# list
'''
x_list = [1,2,3,4,5,6,7,8,9,10]

for x1 in x_list:
    print(x1)

'''

nakama = ['DHAVAL','LUFFY','ZORO','NAMI','USSOP','SANJI','MERRY']

for x in range(len(nakama)):
    print(x,nakama[x])
