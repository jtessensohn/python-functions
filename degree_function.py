C= int(input("Temperature in C? "))

def deg(C):
    return str((9/5)*C + 32)

degree = deg(C)
print(degree + "F")