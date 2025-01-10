# Disneyland Theme Park Annual Passes

import datetime

Total = 0
amt = 0
pass_type = ' '

now = datetime.datetime.now()
print(f"\n Date: {now:%Y-%m-%d %H:%M:%S} \n")  # The Date and Time imported from the datetime library

myName = input("What is your name ? \n").upper()
print()

while pass_type != 'q':

    print(f"Welcome to DisneyLand Ticketing Services {myName} !!\n") # welcoming the user by calling the users name
  
    pass_type = { "silver" : 499.000,
                "gold" : 849.000,
                  "platinum" : 1249.000,}   #mydictonary 

    print("Silver Pass per person is $", pass_type["silver"])
    print("Gold Pass per person is $", pass_type["gold"])
    print("Platinum Pass per person is $", pass_type["platinum"])

    print()
    print(" S - Silver")
    print(" G - Gold")
    print(" P - Platinium")
    print(" Q - Quit")
    print()

    pass_type = input(f"What type of pass would you like to purchase {myName} ? \n").lower() # Converts user input to Lowercase
    print()

    if pass_type == 'q':      #QUIT
        break  # quits the loop immediately

    elif pass_type == 's':    #SILVER
        amt = 499.00
        
    elif pass_type == 'g':    #GOLD
        amt = 849.00

    elif pass_type == 'p':  #PLATINUM
        amt = 1249.00
        
    else:               
        print(f"Oops! invalid entry {myName} please enter S, D, P or Q.\n")
        continue   # continuing the loop after an invalid choice
    
    numPass = int( input(f"How many Disneyland Passes would like to purchase {myName} ? \n") )  # number of passes 
    print() 

    Total = amt * numPass
    print(f"{myName} your Total due for the Theme Park Passes is ${Total:.2f}\n") # total due after picking number of tickets

    print("Each annual parking pass is $125")
    print()
    park_pass = int( input(f"How many Annual Parking Passes whould you like to buy {myName} ?\n") ) # asking the user if they need a parking pass
    print()

    Total = Total + (park_pass * 125)
    print(f"{myName} your subtotal due for Theme Park passes and Parking passes is ${Total:.2f}\n") # the total after adding the parking pass fees

    club_33 = input(f"Are you a member of Club 33 {myName} ?\nY/N \n").lower() # making the output lower case
    print()
    if (club_33 == 'y'):
         Total = Total - (Total * 0.1)
         print(f"{myName} your Total after your Club 33 discount is ${Total:.2f}\n")
    
    Total = Total + (Total*0.095)
    print(f"{myName} your Total Amount due, including taxes is ${Total:.2f}")
    print(f"\nHave a nice day {myName}!!")  # calling the users name

    now = datetime.datetime.now()
    print(f"\n Date: {now:%Y-%m-%d %H:%M:%S} \n") # The Date and Time imported from the datetime library

    print("--------------------------------------------------------------------------------------------")

print(f"\n     Have a nice day {myName}!!") # outside the while loop

now = datetime.datetime.now()
print(f"\n Date: {now:%Y-%m-%d %H:%M:%S} \n") # The Date and Time imported from the datetime library

print("--------------------------------------------------------------------------------------------")
    
                        
