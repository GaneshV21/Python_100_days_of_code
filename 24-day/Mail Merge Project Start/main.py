#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    name_list=names.readlines()
    new_name=[]
for name in name_list:
    new_name.append(name.strip())
for name in new_name:
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_data=letter.read()
        update_text=letter_data.replace("[name]",name)
        with open(f"./Output/ReadyToSend/{name}.txt",mode='w') as mail:
            mail.write(f"{update_text}")






