
def hello(to="Hello"):
    print("hello", to)

def square(n):
    return n ** 2
#or return pow(n,2)

def main():
    name = input('enter your name')
    hello(name)
    n = int(input('enter a number'))
    print(square(n))

main()