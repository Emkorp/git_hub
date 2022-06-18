hours = float(input("How many hours did you work: "))
rate = float(input("What is your rate?: "))
bonus = float(input("Bonus?: "))


def salary():
    return hours * rate + bonus


print(salary())
