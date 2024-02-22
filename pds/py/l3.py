#lecture 1 CS-50
#Conditionals

'''
x = int(input('enter x'))
y = int(input('enter y'))

if x < y:
    print("x is less thsn y")
elif x > y:
    print("y is less thsn x")
else:
    print("both are equal")



if x > y or x < y:
    print("x is not equal to y")
else:
    print("both are equal")



if x!=y:
    print("x is not equal to y")

if x==y:
    print("x is equal to y")



score= int(input("score:"))

if score <= 100 and score >= 0:
    print("Valid entry")
    if score >= 90:
        print('A')
    elif score >= 50:
        print('B')
    elif score >= 23:
        print('PASS')
    else:
        print('Fail')
else:
    print('Invalid entry')


def main():
    y = int(input('enter y'))
    #even_or_odd(x)
    if even_or_odd(y):
        print('EVEN')
    else:
        print('ODD')

def even_or_odd(x):
#    if x % 2 == 0:
#        print('EVEN')
#    else:
#        print('ODD')

    #return True if x % 2 == 0 else False
    return x%2==0


main()
'''
# switch case

day = input("enter day")

match day:
    case 'sunday':
        print('enjoy')
    case 'monday':
        print('work')
    case _:
        print("Not available")