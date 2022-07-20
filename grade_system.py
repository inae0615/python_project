
coffee=3
bubble=2

while True:
    print("*"*20)
    print(" Welcome to \n LIA's cafe")
    print("*"*20)
    print("MENU\n1. coffee \n2. bubble tea")
    print("*"*20)
#1
    seclection=eval(input("Make a selection from the menua(You Should input number 1 or 2): "))
    if seclection==1:
        quantity=int(input("You chose coffee \nGive quantity of coffee: "))
        if seclection==1 and coffee>=quantity: 
            print("Here is what you orderd Thank you!")
            coffee-=quantity
        else:
            print("There is",coffee,"cups left")
#2        
    elif seclection==2:
        quantity=int(input("You chose bubble tea \nGive quantity of bubble tea: "))
        if seclection==2 and bubble>=quantity: 
            print("Here is what you orderd. Thank you!")
            bubble-=quantity
        else:
            print("There is",bubble,"cups left")   
#3   
    else:
        print("Not on the menu")

#4    
    if coffee==0 and bubble==0:
            print("="*20)
            print(" All sold out \n LIA's cafe closed")
            break
        

    
