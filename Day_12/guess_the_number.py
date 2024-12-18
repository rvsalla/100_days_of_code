import random

print('''
 _____                       _   _            _   _                 _                
|  __ \                     | | | |          | \ | |               | |               
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|    
                                                                                     
                                                                                     
''')

attempts = 0

won_game = False

def dificulty_check (dificulty):
    if dificulty == 'H':
        return 5
    elif dificulty == 'E':
        return 10
    else:
        print("Choose a valida option!\n")
        return 0

def guess_check(answer, guess, att):
    if guess == answer:
        print(f"\nCongratulations you won! The answer is {answer}!\n")
        return 0, True
    elif answer > guess:
        print("\nToo low.")
        return att - 1, False
    else:
        print("\nToo hight.")
        return att - 1, False

print("I'm thinking of a number between 1 and 100. \n")

while attempts == 0:
    attempts = dificulty_check(input("Choose you dificulty: Type 'E' for easy mode or 'H' for hard mode: ").upper())

number_to_guess = random.randint(1,100)

#print(number_to_guess)

while attempts > 0 :
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    palyer_guess = int(input("Make a guess: "))
    attempts, won_game = guess_check(number_to_guess, palyer_guess, attempts)
    if attempts > 0 and won_game == False:
        print("Guess again.")

if won_game == False:
    print ("You run out of attempts. Restart the game!\n")
    