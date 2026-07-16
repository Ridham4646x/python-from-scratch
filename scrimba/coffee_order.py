# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total price


totalPrize = 0
drinkCount = 0

name = str(input(" Good morning , please enter your good Name : "))
while(True):
    order = str(input(f" Mr./Mrs. {name} please enter your order( done | latte | americano | expresso) : "))

    if(order == "done"):
        break
    elif(order == "latte"):
        print("here's your order,  latte")
        totalPrize += 3.50
        drinkCount += 1

    elif(order == "americano"):
        print("here's your order, americano")
        totalPrize += 3.00
        drinkCount += 1

    elif(order == "expresso"):
        print("here's your order, expresso")
        totalPrize += 2.50
        drinkCount += 1
    else:
        print('enter a valid order name')
        continue

print("----------INVOICE-------------")
print(f"Total amount : {totalPrize}")
print(f"total drink received : {drinkCount}")