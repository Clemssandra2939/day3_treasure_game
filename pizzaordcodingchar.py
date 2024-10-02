# print("Welcome to Python Pizza Deliveries! ")
# size=input("what size pizza do you want? small,medium or large ")
# bill=0

# if size == "small":
#     bill=+15
#     print(f"pay ${bill}")

# elif size == "medium":
#     bill=+20
#     print(f"pay ${bill}")
# else:
#     bill=+25
#     print(f"pay ${bill}")
# 
# add_pepperoni=input("do u want pepperoni? Yes or No ")
# if add_pepperoni=="Yes":
#         if size =="small":
#             bill+=2
#         else:
#             bill+=3
            
# extra_cheese= input("do u want extra cheese? Yes or No ")
# if extra_cheese=="Yes":
#                 bill +=1
                
#                 print(f"Your final bill is ${bill}")
# 
# 
#  # Logical operator
# having diferent conditions in the same line 
# if condition1 &c condition2 & condition3:
#     do A
#     else:
#   do B

# And,or,not is really useful when it comes to logical operator
# "And"operator
# (A and B) means that both A and B for the entire line of code should be True
# if one of them is False,the overall thing will be False

# "Or"operator
# (A or B) means that if a A or B condition is True or if thet are both True
# when both condition is False then it is False

# "Not" operator
# it reverses a condition...so if a condition is True,then it becomes False
# if it`s` False,then it is True


#Roller coaster program
print("welcome to the rollercoaster!")
height=int(input("what is ur height in cm? "))
bill=0

if height >= 120:
    print("u can ride the rollercoaster!")

    age=int(input("what is ur age? "))
    if age < 12:
      bill=5
      print("child ticket is 5$")

    elif age <= 18:
     bill=7
     print("youth ticket is 7$")

    elif age >= 45 and age <= 55:
      bill=0
      print("Midlife crisis ticket is 0$")

    else:
     bill=12
     print("Adult ticket is 12$")

   
    want_photo=input("do u want a photo taken? Yes or No  ") 
    if want_photo=="Yes":
     bill += 3

    print(f"Your final bill is {bill}$")

else:   
    print("Sorry,u have to grow taller before u can ride.")
    