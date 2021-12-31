import time 
import random

buns= ["sesame bun", "potato bun", "brioche bun", "white bun"]
topping = ["onion", "lettuce", "tomato", "pickels", "hot peppers", "cucumbers", "avacado", 
           "jalapeno", "fries"," onion rings", "fried egg", "cheese", "musturd", "relish", "ketchup", "chipotle", "hotsauce"]
patty= ["salmon", "hamburger", "grilled turkey", "grilled chicken", "breaded chicken", "veggie" ]

print("Thank you for choosing us, The Grand Ole burgermakers, to satisfy your burger cravings!")
time.sleep(2) 
print("We have many options for the possible toppings for your burger!")
time.sleep(2)

ord=input("Would you like to build your burger(1) or are you feeling lucky(2)? (Please choose option 1 or 2)")

if ord=="1":
    Finalorder=[]
    toppingopts=[]
    print ("Here are your options.")
    time.sleep(1)
    print ('toppings:' , topping)
    time.sleep(1) 
    print ('buns:' , buns)
    time.sleep(1) 
    print ('patty' , patty)
    time.sleep(2) 
    bun_opt = input("From the options above, what bun would you like?")
    
    if bun_opt in buns:
        print("This option is viable.")
        Finalorder.append(bun_opt)
    else: 
        print("This option is not viable, please restart order.")
    
    patty_opt = input("From the options above, what patty would you like?")
    if patty_opt in patty:
        print("This option is viable.")
        Finalorder.append(patty_opt)
    else: 
        print("This option is not viable, please restart order.")
    
    toppingamount=int(input("How many toppings you will have? (enter a number)"))
    for number in range(toppingamount):
        topping_opt = input("From the options above, what topping would you like?")
        if topping_opt in topping:
            print("This option is viable.")
            Finalorder.append(topping_opt)
        else: 
            print("This option is not viable, please restart order.")
        
    print ('Your order will be ', Finalorder + toppingopts)
    print ('It will cost $' , (4)+ toppingamount*0.5)
    print ("Thank you")
    
elif ord=="2":
    cost=int(input("How many toppings you will have? (enter a number)"))
    time.sleep(1) 
    bun_pick= random.choices(buns,k=1)
    print ('Your bun will be', bun_pick)
    time.sleep(1) 
    patty_pick= random.choices(patty,k=1)
    print ('Your patty will be', patty_pick)
    time.sleep(1) 
    topping_pick= random.choices(topping,k=cost)
    print ('Your topping(s) will be', topping_pick)
    time.sleep(2) 
    finalorder= [bun_pick, patty_pick, topping_pick]
    print ('Your order will be ', finalorder)
    print ('It will cost $' , (4)+ cost*0.5)
    time.sleep(1) 
    print ("Thank you")

else: 
    print (ord)