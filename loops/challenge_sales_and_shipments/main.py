# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# Subtract units sold
for i in range(len(products)):
    initial_stock = products[i][1]
    sold_stock = units_sold[i][1]
    after_sold_update = initial_stock - sold_stock
    products[i][1] = after_sold_update
    #print(after_sold_update)
    #print(products)

# Add shipments received
for i in range(len(products)):
    received_stock = shipment_received[i][1]
    products[i][1] += received_stock  # fix: update products list directly
    #print(products)

# Print final stock levels
print("Final stock levels for all products:", products)