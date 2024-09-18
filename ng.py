import random
playing=True
number=str(random.randint(10,20))
print("I will genrate a number from 0 to 9 and you have a guess the number digit at a time")
print("Game ends when you 1 Hero")
while playing:
    guess=input("give me your best guess!\n")
                if number ==guess:
                print("you  win the game")
                Print("the number was", number)
                 break 
                else:
                print("Your guess is not right,try again.\n")
    