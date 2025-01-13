import random

numbers = [1,2,3]
new_numbers = [n*2 for n in range(1,5) if n%2 == 0]
print(new_numbers)

names = ['roberta', 'luciano', 'gilmar', 'braulio', 'malaquias']
upper_names = [name.upper() for name in names]
print(upper_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** .5 for n in numbers]
print(squared_numbers)

names2 = ['roberta', 'luciano', 'gilmar', 'braulio', 'malaquias']
names_score = {n:random.randint(1,100) for n in names2}
print(names_score)

pass_names = {name:score for (name, score) in names_score.items() if score > 60}
print(pass_names)

