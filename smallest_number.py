number_list = [11, 20, 42, 97, 23, 10]

def smallest(list):
    for i in range(len(number_list)):
        min1 = number_list[0]
        if number_list[i] < min1:
            min1 = number_list[i]
            return min1

result = smallest(number_list)
print(result)
