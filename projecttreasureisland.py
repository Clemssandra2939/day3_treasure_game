print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
# N.B the three single quote added with the print statement in the beginning and the end of the tresure box is used to create multiple lines of strings
print("Welcome to Treasure Island!")
print("your mission is to find the treasure")
want_to_go=input("You\'re at the crosswalk.Where do u want to go? Type 'left' or 'right' \n").lower()

if want_to_go=="left":
    print("left")
    middle_lake=input("You \'ve come to a lake.There is an island in the middle of the lake.Type'wait'to wait for a boat.Type 'swim'to swim across\n").lower()
    if middle_lake=="wait":
        colour_house=input("You have arrive the island unharmed.there is a house with a red,blue,yellow door.Which door are you going for?\n").lower()
        if colour_house=="red":
            print("This room is full of fire.Game Over!!")
        elif colour_house == "yellow":
            print("You found the Treasure.You won!!") 
        elif colour_house == "blue":
            print("This room is full of water,you drowned.Game Over!!")
        
        else:
            print("You entered a endless doors of chaos.Game Over!!")
    else:
        print("You are eaten by angry crocodiles.Game Over!!")
else:
    print("You fell into a hole.Game Over!!")
