
Name = input("Enter your surname:")

LastName = input("Enter your last name:")

FullName = Name+" "+LastName

# print(LastName,Name)

print("Hello, {} {}".format(FullName.casefold().title().split()[1],FullName.casefold().title().split()[0]))
