with open("newfile3.txt", "r") as my_file3:
    less = []
    aver_sal = []
    my_list = my_file3.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            less.append(i[0])
        aver_sal.append(i[1])

print(f'Salary less than 20.000 {less}, average salary {sum(map(int, aver_sal)) / len(aver_sal)}')

