number_list = [11, 20, 42, 97, 23, 10]

def largest(list):
    for i in range(len(number_list)):
        max1 = number_list[0]
        if number_list[i] > max1:
            max1 = number_list[i]
            return max1

result = largest(number_list)
print(result)
