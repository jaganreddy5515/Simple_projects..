from ast import Break
import random


def game():

    user_choice=input("Enter your choice ")


    products=['snake','water','gun']
    if(user_choice not in products):
        print("Invalid choice")
    computer_choice=random.choice(products)
    print(f"computer choice is : {computer_choice}")
    if(user_choice==computer_choice):
        print("Its a tie ....")


    elif(user_choice=="snake" ):
        if(computer_choice=="water"):
            print("Snake drinks water ... user wins")
            asking()

        else:
            print("Gun kills snake.. computer wins")  
            asking()  
    elif(user_choice=="water"):
        if(computer_choice=="gun"):
            print("Water wins... user wins") 
            asking()       
        else:
            print("Snake drinks water.. computer wins")
            asking()
    elif(user_choice=="gun"):
        if(computer_choice=="snake"):
            print("GUn kills the snake.. user wins")
            asking()
        else:
            print("water wins ... computer wins")
            asking()

def asking():

    ask=input("You want to play again (Y/N) ")
    if(ask=='y'.lower()):
        game()
    elif(ask=='n'.lower()):
        Break
    else:
        asking()

user=input("\nEnter your name  ")
print(f"WELCOME {user} TO SNAKE WATER GUN GAME ")
print("select your choice\n1:snake\n2:water\n3:gun")
j=("gun","water","snake")
game()
