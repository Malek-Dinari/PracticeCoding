
filename = input("Choose your file name: ")


while True:
        
    if ("." not in filename or filename.count(".")>1):

        filename=input("Please enter a valid file name with an extension: ")
        
    else:
        
        output = filename.split(".")[-1]
        print(output)
        break