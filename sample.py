from ast import Break, Del
from ast import Break
from itertools import islice 


item={}

def juice_menu():
    print("-"*30)
    juice_input=int(input("1.Mango juice-----$ 20\n2.Pinaple juice-----$ 30\n3.Apple juice-----$ 40\n4.return MAIN MENU\n"))
    if(juice_input==1):                                         # mango juice
        juice_qty=int(input("Enter quantity..\n"))        
        total=print("Amount of mango juice = ",20*juice_qty)
        total_m=20*juice_qty
        confirm_mango=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_mango==1):
            item.update({'Mango ->':total_m})
            # items.append(total_m)
            print("Order confirmed \n")
            juice_menu()                                        # common juice menu
        elif(confirm_mango==2):
            print("Order cancelled..\n")
            juice_menu()
        else:
            print("invalid choice..\n")
            juice_menu()

    
    elif(juice_input==2):
        juice_qty_p=int(input("Enter quantity..\n"))
        total_p=print("Amount = ",30*juice_qty_p)
        total_p_i=30*juice_qty_p
        confirm_pinaple=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_pinaple==1):
            item.update({'Pinaple ->':total_p_i})
            # items.append(total_p_i)
            print("Order confirmed \n")
            juice_menu()                                        # common juice menu
        elif(confirm_pinaple==2):
            print("Order cancelled..\n")
            juice_menu()
        else:
            print("invalid choice..\n")
            juice_menu()
    
    elif(juice_input==3):
        juice_qty_a=int(input("Enter quantity..\n"))
        total_a=print("Amount = ",40*juice_qty_a)
        total_a_i=40*juice_qty_a
        confirm_apple=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_apple==1):
            item.update({'Apple ->':total_a_i})

            print("Order confirmed \n")
            juice_menu()
        elif(confirm_apple==2):
            print("Order cancelled..\n")
            juice_menu()
        else:
            print("invalid choice..\n")
            juice_menu()

    elif(juice_input==4):
        main_menu()
    

    else:
        print("Invalid choice..\n")
        juice_menu()



def cold_menu():
    print("-"*30)
    cold_drink=int(input("1.Sprit-----$ 20\n2.Maaza-----$ 25\n3.Pepsi-----$30\n4.Back to Main Menu\n"))
    if(cold_drink==1):
        cold_qty=int(input("Enter the quantity..\n"))
        print("Amount = ",20*cold_qty)
        total_s=20*cold_qty
        confirm_sprit=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_sprit==1):
            item.update({'Sprit ->':total_s})
            # items.append(total_s)
            print("Order confirmed..\n")
            cold_menu()
        elif(confirm_sprit==2):
            print("Order cancelled..\n")
            cold_menu()
        else:
            print("Invalid choice..")
            cold_menu()

    elif(cold_drink==2):
        cold_qty_m=int(input("Enter the quantity..\n"))
        print("Amount = ",25*cold_qty_m)
        total_maaza=25*cold_qty_m
        confirm_maaza=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_maaza==1):
            item.update({'Maaza ->':total_maaza})
            # items.append(total_m)
            print("Order confirmed..\n")
            cold_menu()
        elif(confirm_maaza==2):
            print("Order cancelled..\n")
            cold_menu()
        else:
            print("Invalid choice..")   
            cold_menu()


    elif(cold_drink==3):
        cold_qty_p=int(input("Enter the quantity..\n"))
        print("Amount = ",30*cold_qty_p)
        total_pep=30*cold_qty_p
        confirm_pepsi=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_pepsi==1):
            item.update({'Pepsi ->':total_pep})
            # items.append(total_p)
            print("Order confirmed..\n")
            cold_menu() 
        elif(confirm_pepsi==2):
            print("Order cancelled..\n")
            cold_menu()
        else:
            print("Invalid choice..")                   
            cold_menu()

    elif(cold_drink==4):
        main_menu()
    else:
        print("Invalid choice..\n")
        cold_menu()


def foods_menu():
    print("-"*30)
    foods=int(input("1.mutton biryani-----$ 250\n2.chicken biryani-----$ 200\n3.veg biryani-----$ 150\n4.back to Main Menu\n"))
    if(foods==1):
        foods_m=int(input("Enter the quantity..\n"))
        print("Amount",250 * foods_m)
        total_mutto=250*foods_m
        confirm_mutton=int(input("press 1 to confirm order\npress 2 to cancel order\n"))
        if(confirm_mutton==1):
            item.update({'Mutton biryani ->':total_mutto})
            # items.append(total_m)
            print("Order confirmed..\n")
            foods_menu() 
        elif(confirm_mutton==2):
            print("Order cancelled..\n")
            foods_menu()
        else:
            print("Invalid choice..") 
            foods_menu()

    
    elif(foods==2):
        foods_c=int(input("Enter the quantity..\n"))
        print("Amount",200 * foods_c)
        total_chic=250*foods_c
        confirm_chicken=int(input("press 1 to confirm order\npress 2 to cancel order\n"))  
        if(confirm_chicken==1):
            item.update({'Mango ->':total_chic})

            print("Order confirmed..\n")
            foods_menu() 
        elif(confirm_chicken==2):
            print("Order cancelled..\n")
            foods_menu()
        else:
            print("Invalid choice..")
            foods_menu()

    elif(foods==3):
        foods_v=int(input("Enter the quantity..\n"))
        print("Amount",150 * foods_v)
        total_veg=150*foods_v
        confirm_veg=int(input("press 1 to confirm order\npress 2 to cancel order\n"))  
        if(confirm_veg==1):
            item.update({'Mango ->':total_veg})

            print("Order confirmed..\n")
            foods_menu()
        elif(confirm_veg==2):
            print("Order cancelled..\n")
            foods_menu()
        else:
            print("Invalid choice..")
            foods_menu()

    elif(foods==4):
        main_menu()

    else:
        print("Invalid choice..\n")
        foods_menu()


def cart1():
    print("\n")

    for a,b in enumerate(item.items()):
        print(a,b)

    cart=int(input("\n1.BACK to main menu\n2.REMOVE items from cart\n3.pay amount\n"))
    if(cart==1):
        main_menu()
    elif(cart==2):
        n=int(input("\n1.To remove specific items\n2.Remove all items from your cart\n"))
        if(n==1):
            nm=int(input("\nEnter item number to remove\n"))
            # item.pop(nm)
            del item[next(islice(item, nm, None ))]
            print("\nRemaining items...")
            cart1()
        elif(n==2):

            item.clear()
            print("Cart empty..\n")
            main_menu()
    elif(cart==3):
        print("1.PhonePay\n2.GooglePay\n3.Paytm\n")
        print("Payment temporary unable...\n")
        cart1()
    else:
        print("Invalid choice..")
        cart1()


def main_menu():                                    
    print("\n")
    print("*"*100)
    a=int(input("1.juice\n2.cold drinks\n3.foods\n4.View cart\n5.Exit\n"))
    if(a==1):
        juice_menu()
    elif(a==2):
        cold_menu()
    elif(a==3):
        foods_menu()
    elif(a==4):
        cart1()
    elif(a==5):
        Break
    else:
        print("Invalid choice..\n ")
        main_menu()

        




main_menu()
