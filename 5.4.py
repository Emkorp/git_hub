
import shutil
import os
shutil.copyfile('file4.txt', 'file4.txt.copy')
my_file4 = open("file4.txt.copy")
my_list = my_file4.readline()


print(my_list.replace('One', 'один'))
my_list2 = my_file4.readline()
print(my_list2.replace('Two', 'два'))
my_list3 = my_file4.readline()
print(my_list3.replace('Three', 'три'))
my_list4 = my_file4.readline()
print(my_list4.replace('Four', 'четыре'))
my_file4.close()






