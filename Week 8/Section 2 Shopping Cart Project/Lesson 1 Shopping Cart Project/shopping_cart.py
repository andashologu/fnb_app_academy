# Create a shopping cart programme that will continously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to thier cart
# At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the prioce of the {food}: R"))
        foods.append(food)
        prices.append(price)

print("--------YOUR CART-------")

for food in foods:
    print(food, end= " ") # 'end' replaces default /n
    
for price in prices:
    total += price # total = total + price
print("\n")
print(f"Your total is: R{total}")
    