def add(*args): 
    sum = 0
    for n in args:
        sum += n
    print(type(args))
 
add(1,2,3,4,5,6,7,8,9)