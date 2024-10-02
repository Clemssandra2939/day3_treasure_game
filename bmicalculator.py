# height=float(input("enter ur height in m: "))
# weight=float(input("enter ur weight in kg: "))
# bmi=round(weight/height**2)
# if bmi < 18.5:
#     print("you are slightly underweight")
# elif bmi > 25:
#     print("you have a normal weight")
# elif bmi < 30:
#     print("you are slightlly overweight")
# elif bmi < 35:
#     print("you are slightl obese")
# else:
#     print("you are clinically obese")

# Multiple If tatements in Succession

# if/elif/else
# if condition1:
#     do A
# elif condition2:
#     do B
#     else:
#   do C

# Multiple if
# if condiion1:
#     do A
# if conditon2:
#     do B
#     if condtion3:
#         do C

# this occurs when the three If statements id true,then all of them is excuted

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

    else:
     bill=12
     print("Adult ticket is 12$")

    want_photo=input("do u want a photo taken? Yes or No  ") 
    if want_photo=="Yes":
     bill += 3

    print(f"Your final bill is {bill}$")

else:   
    print("Sorry,u have to grow taller before u can ride.")

# #   here if they are below 12 they pay 5$ 
# # if they are 12 to 18 they pay $7 buh if they greater than 18 they pay adult price 12$
