F= int(input("Temperature in F? "))

def deg(F):
    return str((F - 32) * 5/9)

degree = deg(F)
print(degree + "C")