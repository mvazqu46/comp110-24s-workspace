"""EX01 - Simple Battleship! """
__author__= "730718822"
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
SHIP: str = "\U0001F7E6" + "\U0001F7E6" + "\U0001F7E6"
msg1: str = " too low!"
msg2: str = " too high!"
user_input: str = input("Pick a secret boat location between 1 and 4: ")
user_number: int = int(user_input)
user_input2: str = input("Guess a number between 1 and 4: ")
user_number2: int = int(user_input2)
if user_number > 4:
    print ("Error! " + str(user_number2)+ str(msg2))
    exit()
elif user_number <1:
    print("Error! "+ str(user_number2)+ str(msg1))
    exit()
if user_number2 > 4:
    print ("Error! " + str(user_number2)+ str(msg2))
    exit()
elif user_number2 <1:
    print("Error! "+ str(user_number2)+ str(msg1))
    exit()
if user_number2 == user_number:
    print(str(RED_BOX)+ str(BLUE_BOX) + str (BLUE_BOX)+ str(BLUE_BOX)) 
elif user_number2 != user_number:
    print(str(WHITE_BOX)+ str(BLUE_BOX)+ str(BLUE_BOX) + str(BLUE_BOX))
    if user_number2 == user_number:
        print(str(BLUE_BOX) + str(RED_BOX)+ str(BLUE_BOX) + str (BLUE_BOX)) 
    elif user_number != user_number: 
        print(str(BLUE_BOX) + str(WHITE_BOX)+ str(BLUE_BOX)+ str(BLUE_BOX))
        if user_number2 == user_number:
            print(str(str(BLUE_BOX) + str (BLUE_BOX)+ RED_BOX)+ str(BLUE_BOX)) 
elif user_number2 != user_number:
    print(str(BLUE_BOX)+ str(BLUE_BOX) + str(WHITE_BOX)+ str(BLUE_BOX))
    if user_number2 == user_number:
        print(str(BLUE_BOX) + str(BLUE_BOX) + str (BLUE_BOX)+ str(RED_BOX)) 
elif user_number2 != user_number: 
    print(str(BLUE_BOX)+ str(BLUE_BOX)+ str(BLUE_BOX) + str(WHITE_BOX))
if user_number2 == user_number:
    print("Correct! You hit the ship." )
else: 
    print("Incorrect! You missed the ship." )
