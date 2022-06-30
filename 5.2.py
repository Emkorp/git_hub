myfile_f = open("newfile.txt")
inside = myfile_f.readlines()

number_string = len(inside)


myfile_f = open("newfile.txt")
words1 = myfile_f.readline()
first_string = words1.split()

words2 = myfile_f.readline()
second_string = words2.split()

print("There are " + str(number_string) + " strings in the file and in the first string " + str(len(first_string)) + " words and in the second string " + str(len(second_string)) + " word")
myfile_f.close()


