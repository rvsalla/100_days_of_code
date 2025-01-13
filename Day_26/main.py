#student_dict = {
#    "student": ["Angela", "James", "Lily"], 
#    "score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
    #pass

#import pandas
#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

nato_df = pd.read_csv(r'C:\Python\100_days_of_code\Day_26\nato_phonetic_alphabet.csv')

name = input("Enter a word: ").upper()

nato_dic = {row.letter:row.code for (index, row) in nato_df.iterrows()}

nato_list = [nato_dic[letter] for letter in name ]

print(nato_list)

