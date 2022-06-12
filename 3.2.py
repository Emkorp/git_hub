def func():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    birth = input("Enter your date of birth: ")
    city = input("Enter city you are living: ")
    email = input("Enter email: ")
    phone = input("Enter your phone number: ")
    return (name, surname, birth, city, email, phone)

name, surname, birth, city, email, phone = func()
print(f"Name - {name}; surname - {surname}, birth - {birth}, city - {city}, email - {email}, phone  - {phone}")
