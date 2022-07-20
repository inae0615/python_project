
#1
class Cafe():
    def __init__(self, named_name,named_quantity):
        self.named_name = named_name
        self.named_quantity = named_quantity
        
        
class Food(Cafe):
    def __init__(self, named_name,named_quantity, named_warming):
        Cafe.__init__(self,named_name,named_quantity)
        self.named_warming=named_warming
        
#2
def main():
  cafe = {}
  while(1):
    n = int(input("Do you want to continue? (yes=1/no=2) : "))
    if n == 1:
        name = input("Enter the menu's name: ")
        try:
            qty = int(input("Enter the initial quantity of menu: "))
        except ValueError:
            print("That was no valid number.  Try again...")
            qty = int(input("Enter the initial quantity of menu: "))
        DrinkorFood = input("Enter category (drink or food): ")
        if DrinkorFood == 'food':
          y_n = input("Enter warimg option (warm/cold ) : ")
          if y_n =="warm":
              f = Food(name,qty,True)
          else:
              f = Food(name,qty,False)
        else:
          f = Cafe(name,qty)
        cafe[name] = f
    elif n == 2:
        break
    
#3    
  while True:
    count = 0
    print("*"*20)
    print(" Welcome to \n LIA's cafe")
    print("*"*20)
    print("-----menu------")
    for key, value in cafe.items():
        print(key ,"( quantity =",value.named_quantity,")")
    print()
    print("*"*20)
    menu = input("Make a selection from the menu: ")
    if menu in cafe:
        try:
            quantity=int(input("Please tell me the quantity : "))
        except ValueError:
            print("That was no valid number.  Try again...")
            quantity=int(input("Please tell me the quantity : "))

        if cafe[menu].named_quantity>=quantity: 
            print("Here is what you orderd Thank you!")
            cafe[menu].named_quantity-=quantity
        else:
            print("Sorry. This quantity is insufficient ")
        
    else:
        print("Not on the menu")
   
    for key, value in cafe.items():
        if value.named_quantity ==0:
            count+=1
            
    if count == len(cafe):
        print("="*20)
        print(" All sold out \n LIA's cafe closed")
        break

main()

