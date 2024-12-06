#Set hangman images
hangman = ['''
 +---+
 |   |
 o   |
/|\  |
/ \  |
''',
'''
 +---+
 |   |
 o   |
/|   |
/ \  |
''',
'''
 +---+
 |   |
 o   |
 |   |
/ \  |
''',
'''
 +---+
 |   |
 o   |
 |   |
  \  |
''',
'''
 +---+
 |   |
 o   |
     |
     |
''',
'''
 +---+
 |   |
     |
     |
     |
'''
]
#choose a randon word
import random
word_list = ['meatball','banana','lituania']
word = random.choice(word_list)

#Create the blank spaces to be filled
blank = []
for i in word:
    blank.append("_")

stage = 5
#Make a loop
while "_" in blank and stage > 0:
    #Print hangman and 
    print(hangman[stage])
    print(''.join(blank))

    #Ask for a letter
    guess = input("Guess a letter: ").lower()

    #See if the letter is right
    caracter = 0
    right_letter = 1
    for i in word:
        if i == guess:
            blank[caracter] = guess
            right_letter = 0
        caracter += 1
    stage = stage-right_letter

if stage == 0:
    print(hangman[stage])
    print("You Lose!")
    print(f"The word was {word}")
else:
    print('\n')
    print(''.join(blank))
    print("You Win!")
