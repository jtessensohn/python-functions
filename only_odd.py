number_list = [11, 20, 42, 97, 23, 10]

def only_odd(num):
    only_oddlist = []
    for num in number_list:
        if num % 2 != 0:
            only_oddlist.append(num)
    return only_oddlist

result = only_odd(number_list)

print(result)