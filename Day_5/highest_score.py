student_scores = [1,3,6,12,53,13,54,7,43,4,87,95,43,8,54]

sum = 0
for score in student_scores:
    sum += score
print(sum) 


max = 0
for score in student_scores:
    if score > max:
        max = score
print(max) 

total = 0
for number in range(1,101):
    total += number
print (total)