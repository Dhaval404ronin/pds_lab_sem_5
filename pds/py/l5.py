# Dict
'''
nakama = {'DHAVAL': None,
          'LUFFY':'CAPTAIN',
          'ZORO':'SWORDSMAN',
          'NAMI':'NAVIGATOR',
          'USSOP':'SNIPER',
          'SANJI':'COOK',
          'MERRY':'SHIP'
}

print(nakama['LUFFY'])

print()

for n in nakama:
    print(n,nakama[n],sep=':')
'''

# list[dict] 
#list=[
# {},
# {},
# {}
# ]
'''
nakama = [
    {'NAME':'DHAVAL','ROLE':None,'DREAM':'CHILL EVERYDAY'},
    {'NAME':'LUFFY','ROLE':'CAPTAIN','DREAM':'KING OF THE PIRATES'},
    {'NAME':'ZORO','ROLE':'SWORDSMAN','DREAM':'STRONGEST SWORDSMAN'},
    {'NAME':'NAMI','ROLE':'NAVIGATOR','DREAM':'MAP THE WHOLE WORLD'},
    {'NAME':'USSOP','ROLE':'SNIPER','DREAM':'BRAVE WARRIOR OF THE SEA'},
    {'NAME':'SANJI','ROLE':'COOK','DREAM':'FIND ALL BLUE'},
    {'NAME':'MARRY','ROLE':'SHIP','DREAM':None}
]

for x in nakama:
    print(x['NAME'], x['ROLE'], x['DREAM'],sep=':')

'''


'''
def square(n):
    for i in range(n):
        for j in range(n):
            print('#  ',end='')
        print()
'''

def square(n):
    for i in range(n):
        print('#  '*n)

c = int(input("enter size"))
square(c)
