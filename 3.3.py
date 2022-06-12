def my_func(x, y, z):
    if x > y and z > y :
        return x + z
    if x > z and y > z :
        return x + y
    if y > x and z > x :
        return y + z
print(f'Result - {my_func(int(input("enter 1st argument ")), int(input("enter 2nd argument ")), int(input("enter 3rd argument ")))}')