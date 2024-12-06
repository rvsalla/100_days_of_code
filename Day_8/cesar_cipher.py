#Create a list for alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#create de encryption function
def cesar(direction, original_text, shift_ctd):
    output_text = ""
    for i in original_text:
        if i not in alphabet:
            output_text += i
        else:
            position_caracter = alphabet.index(i)
            if direction == 'e':
                new_caracter = (position_caracter + shift_ctd) % len(alphabet)
            else:
                new_caracter = (position_caracter - shift_ctd) % len(alphabet)
            output_text += alphabet[new_caracter]
    print(output_text)

#begin program
direction = input("Type 'E' to encode or 'D to decode: ").lower()

#check type
if direction in ['d','e']:
    text = input("Type your mensage: ")
    shift = int(input("Type the shift number: "))
    cesar(direction,text,shift)
else:
    print('Wrong encrypt type! Try Again!')
