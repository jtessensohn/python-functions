number = int(input("Which number would you like to check? "))

def is_even(num):
    return (num % 2) == 0

result = is_even(number)
print(result)