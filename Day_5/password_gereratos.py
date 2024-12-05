import random

letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+']

nr_lt = int(input("how many letters? "))
nr_nr = int(input("how many numbers? "))
nr_sb = int(input("how many symbols? "))

lista = []

for i in range (0, nr_lt):
    lista.append(random.choice(letters))

for i in range (0, nr_nr):
    lista.append(random.choice(numbers))

for i in range (0, nr_sb):
    lista.append(random.choice(symbols))

#print(lista)

random.shuffle(lista)

#print (lista)

password = ""
for i in lista:
    password += i

print (f"Your PAssword is {password}")
