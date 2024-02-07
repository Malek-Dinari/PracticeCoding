
seq, user_input="",""

while True:
    
    user_input = input("Add a number to the sequence: ")
    
    if (user_input.isnumeric() and user_input!=""):
        seq +=user_input+" "
        
    else:
        break


    
# Make the tuple  
seq_tuple = tuple(seq.split(" "))
print("Tuple of the sequence: ",seq_tuple[:-1])

# Make the list

seq_list = list(seq.split(" "))
print("List of the sequence: ",seq_list[:-1])