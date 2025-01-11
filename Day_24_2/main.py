#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(".\Day_24_2\Input\Letters\starting_letter.txt", mode= "r") as starting_letter:
        letter_text = starting_letter.read()

with open(r".\Day_24_2\Input\Names\invited_names.txt", mode= "r") as invited_names:
        name_list = invited_names.read().splitlines()

for name in name_list:
       final_letter = letter_text.replace('[name]', name)
       with open(f".\Day_24_2\Output\ReadyToSend\letter_for_{name}.txt", mode= "w") as invite_letter:
             invite_letter.write(final_letter)
