prices = [29.99, 45.50, 12.75, 38.20]
discount_factors = [0.10, 0.20, 0.15, 0.05]

for i in range(len(prices)):
    discount_factor = 1 - discount_factors[i]
    updated_price = prices[i] * discount_factor
    prices[i] = updated_price
    print(f"Updated price for item {i}:${updated_price:.2f}")


    
    
    
    
    

        
        #print(f"Updated price for item {price +1}: ${prices[price]:.2f}")


