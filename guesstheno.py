import random
name = input("Hi, Whats your good name :- ")
print("Hi, "+ name.title() + ", Lets Play a Guess The Number Game")
print("I have guess the number between 1 to 30, Can you guess it correctly\nI will give you 5 Trails for That")
mysecretnum = random.randint(1,30)
# print("DEBUG :- "+str(mysecretnum)) #Uncommemt this part to verify your secret no
for Take_Guess in range (1,6):
    print("Guess the Number Dear "+ name.title())
    guessno = int(input())
    if guessno > mysecretnum:
        print("Your guess no is too high, "+ name.title())
    elif guessno < mysecretnum:
        print("Your guess no is too low, " + name.title())
    else:
        break
if guessno == mysecretnum:
    print("Hurry you are successfully Guess my Secret no " + str(mysecretnum) + " in " + str(Take_Guess) + " guesses!" )
else:
    print("Sorry you cant guess my Secret no " + str(mysecretnum) + ". So lets try your luck with another no " )


# if guessno == mysecretnum:
#     score = Take_Guess * 10
#     if score >=0.8:
#         print("You are Superb, Good Score")
#     else:
#         print("Well Played")
#here is some problem wih scoring, i will solve it, if anyone have solution plese send me on below mention no.

print ("\n*************************************************\nThis code is written by Chetan Tembhare\nMob No :- 9923908696\n*************************************************")

