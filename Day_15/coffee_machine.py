import cm_data

def check_option(option, list):
    loop = True
    while loop == True:
        if option in list:
            loop = False
            return option
        else:
            option = input(f"\nWrong entry, choose a valid option {list[2:len(list)]}: ").upper()

#Create list of valid options to check client option, to improove this see if there is a way to access the vaules in the dictionary directly
option_list = ['REPORT', 'OFF']
for i,j in cm_data.MENU.items():
    option_list.append(j['option'])

def check_resources(cl_option):
    for drink,details in cm_data.MENU.items():
        if details['option'] == cl_option:
            if cm_data.resources ['water'] >= details['ingredients']['water'] and cm_data.resources ['milk'] >= details['ingredients']['milk'] and cm_data.resources ['coffee'] >= details['ingredients']['coffee']:
                return True
            else:
                if cm_data.resources ['water'] < details['ingredients']['water']:
                    print('Sorry there is not enough water.')
                elif cm_data.resources ['milk'] < details['ingredients']['milk']:
                    print('Sorry there is not enough milk.')
                elif cm_data.resources ['coffee'] < details['ingredients']['coffee']:
                    print('Sorry there is not enough coffee.')
                return False

client_option = ''

#print(cm_data.resources)
#cm_data.resources['milk'] -= 100
#print(cm_data.MENU['espresso']['option'])
#def check_opption(c_option):

while client_option != 'OFF':
    if client_option == 'OFF':
        print('Turning off the machine')
    else:
        #Input option
        print(cm_data.LOGO)

        print("Beverage options:\n")

        for i,j in cm_data.MENU.items():
            print(f"Drink: {i}, Menu option: {j['option']}, ${j['cost']}")

        client_option = check_option(input("\nWhat would you like? espresso(E) / latte(L) / cappuccino(C): ").upper(), option_list)

        #Report option
        if client_option == 'REPORT':
            for i, j in cm_data.resources.items():
                if i == 'cofee':
                    print(f"{i}: {j}g")
                else:
                    print(f"{i}: {j}ml")
            print(f"Money: ${cm_data.money['value']}")

        #print(client_option)
        check_resources(client_option)