grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                     "Eggs": ("Dairy", 5.50, 30),
                     "Bread": ("Bakery", 2.99, 15),
                     "Apples": ("Produce", 1.50, 50)
    
}

eggs_details = grocery_inventory["Eggs"]
eggs_price = eggs_details[1]
#print(eggs_price)
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    eggs_price -= 1
else:
    print("The price of is reasonable.")
print(f"Reduced egg price: {eggs_price}")
grocery_inventory.update({"Eggs": ("Dairy", eggs_price, 30)})
print(grocery_inventory)

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_details = grocery_inventory["Milk"]
milk_stock = milk_details[2]
#print(milk_stock)
if milk_stock < 10:
    print("Milk needs to be restocked. increasing stock by 20 units.")
    milk_stock_updated = milk_stock + 20
else:
    print("Milk has sufficient stock.")

grocery_inventory.update({"Milk": ("Dairy", 3.50, milk_stock_updated)})
#print(f"Milk stock: {milk_stock_updated}")
print(f"Updated inventory: {grocery_inventory}")