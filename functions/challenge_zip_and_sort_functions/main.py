# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(tuple(zip(products, prices, quantities_sold)))
sorted_products = sorted(combined_list)
sorted_product_list = [list(item) for item in sorted_products]
print(sorted_product_list)

dic = sorted_product_list

for name, price, quant in sorted_product_list:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {quant} ")
