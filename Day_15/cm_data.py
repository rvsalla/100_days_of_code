LOGO = '''
   _____       __  __                           (  )   (   )  )
  / ____|     / _|/ _|                           ) (   )  (  (
 | |     ___ | |_| |_ ___  ___                   ( )  (    ) )
 | |    / _ \|  _|  _/ _ \/ _ \                  _____________
 | |___| (_) | | | ||  __/  __/                 <_____________> ___
  \_____\___/|_| |_|_\___|\___|                 |             |/ _ \\
 |  \/  |          | |   (_)                    |               | | |
 | \  / | __ _  ___| |__  _ _ __   ___          |               |_| |
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \      ___|             |\___/
 | |  | | (_| | (__| | | | | | | |  __/     /    \___________/    \\
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|     \_____________________/
                                       
'''
MENU = {
    "espresso": {
        "option": "E",
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "option": "L",
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "option": "C",
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}