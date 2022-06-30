new_file = open("newfile.txt", "w+")
while True:
    s = input("Enter text: ")
    if s == ' ': break
new_file.close()
