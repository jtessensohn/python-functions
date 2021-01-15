# Take a user's input for a number, and then print out all of the numbers from 1 to that number.
# For any number divisible by 3, print 'fizz'
# For any number divisible by 5, print 'buzz'
# For any number divisible by 3 and 5, print 'fizzbuzz'
#take user input for initial fizzbuzz length
user_input = int(input("How long do you take your fizz? "))
# attempt a for loop, maybe nest in function
for count in range(1, user_input + 1):
    if count % 15 == 0:
        print('fizzbuzz')
    elif count % 3 == 0:
        print('fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print(count)
