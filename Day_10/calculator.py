def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def times(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    cont = 'y'
    
    number1 = int(input('What is the frist number: '))
    
    while cont == 'y':
        operator = input('Type teh operator (+,-,*,/): ') 
        number2 = int(input('What is the second number: '))
    
        if operator == '+':
            run_function = add
        elif operator == '-':
            run_function = sub
        if operator == '*':
            run_function = times
        if operator == '/':
            run_function = div
    
        result = run_function(number1,number2)
    
        print(f"{number1} {operator} {number2} = {result}")
    
        cont = input(f"Do you wanna contunue calculatint with the result {result}? (y/n)").lower()

        if cont == 'n':
            calculator()
        else:
            number1 = result

calculator()