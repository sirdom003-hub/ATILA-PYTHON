archive = open("users.csv", "a", encoding="utf-8")

name = input("Name: ")
date = input("Date of birth: ")
email = input("Email: ")
login = input("Login: ")
password = input("Password: ")
gender = input("Gender: ")

line = name + ";" + date + ";" + email + ";" + login + ";" + password + ";" + gender + "\n"

archive.write(line)
archive.close()

print("User data saved successfully!")

archive = open("users.csv", "r", encoding="utf-8")

for lines in archive:
    data = lines.strip().split(";")
    
    print("Name:", data[0])
    print("Date of birth:", data[1])
    print("Email:", data[2])
    print("Login:", data[3])
    print("Password:", data[4])
    print("Gender:", data[5])
    print("-" * 40)
    
archive.close()
    