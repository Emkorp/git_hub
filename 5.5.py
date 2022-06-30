myfile = open("newfile5.txt", 'w')
myfile.write(input("Enter numbers with backspace: "))
myfile = open("newfile5.txt").read().split()
lst = []
for i in myfile:
    if i.isdigit():
        lst.append(int(i))
print(sum(lst))

