# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(price, quantity_sold):
    revenue = [p * q for p,q in zip(price, quantity_sold)]
    return revenue
    
def formatted_output(revenues):
    for product, revenue in sorted(revenues):
        print(f"{product} has total revenue of ${revenue}.")
     
my_revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, my_revenue))
formatted_output(revenue_per_product) 



# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")