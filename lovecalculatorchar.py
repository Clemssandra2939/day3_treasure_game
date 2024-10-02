# check love score between two people
# take both peoplethe letters names ad check for the number of times
# the letter in the word TRUE occurs.
# then check for the number of times the letter in thr word LOVE occurs.octthen combine these umbers to make a 2 digit number.
#

# how to use a lowercase and count function,it can be used to change capital letters to small and for counting alphabets of a string
# print("Angela".lower())
# print("Angela".count("a"))


# lower_case_name=("Angela".lower())
# print(lower_case_name.count("a"))

# Love calculator challenge
print("Welcome to love calculator!")
name1=input("What is your name?\n")

name2=input("What is his name?\n")


our_names=name1 + name2

lower_case_string=our_names.lower()
print(lower_case_string)


t=our_names.count("t")
r=our_names.count("r")
u=our_names.count("u")
e=our_names.count("e")

true=t+r+u+e

l=our_names.count("l")
o=our_names.count("o")
v=our_names.count("v")
e=our_names.count("e")

love=l+o+v+e

love_score=int(str(true)+str(love))


if love_score < 10 or love_score > 90:
    print (f"your score is {love_score},you go together like coke and mentos")    
elif love_score >= 40 and love_score <= 50:
    print (f"your score is {love_score},you are alright together")
else:
    print (f"your score is {love_score} ")
