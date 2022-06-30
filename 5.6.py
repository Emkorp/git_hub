
myfile_f = open("file6.txt")
my_list = myfile_f.read().split("\n")[:-1]

dict = dict()

for item in my_list:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
print(dict)
myfile_f.close()

