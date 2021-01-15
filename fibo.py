# Write a program that asks the user for a numerical input 'n'
# It will then print out the corresponding fibonacci sequence 
# values from 0 to 'n'

user_input = int(input("Please enter a number: "))
def fib(n):
    x = 0
    y = 1
    while x <= n:
        print(x, end=" ")
        x, y = y, x + y
    print()

fib(user_input)
