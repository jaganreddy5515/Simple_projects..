from ast import Break
import random
   
def again_game():
    again=input("Do you want to play again..? ( Y/N )  ")
    if(again.lower()=="y"):
        game()
    elif(again.lower()=="n"):
        Break
    else:
        again_game()

def game():
    print("You have 15 chances")
    rand_num=random.randint(2,1000)
    count=15
    user=1
    while(user!=rand_num):
        if(count==0):
            print(f"You loose the game\nActual Number is {rand_num}  ")
            again_game()    
            break
        else:
            user=int(input('Guess a number '))
            if(user==rand_num):
                print("You won the game..")
                again_game()
            elif(user>rand_num):
                print("You guessed too large..")
                count=count-1
                print(f"Remaining chances {count} \n")
            elif(user<rand_num):
                print("You guessed too small..")
                count=count-1
                print(f"Remaining chances {count} \n")

def intro():
    name=input("Enter your name.. ")
    print(f"Welcome {name.upper()} to Guessing Game ")
    game()

intro()
            


    

