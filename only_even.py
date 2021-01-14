number_list = [11, 20, 42, 97, 23, 10]

def only_even(num):
    only_evenlist = []
    for num in number_list:
        if num % 2 == 0:
            only_evenlist.append(num)
    return only_evenlist

result = only_even(number_list)

print(result)