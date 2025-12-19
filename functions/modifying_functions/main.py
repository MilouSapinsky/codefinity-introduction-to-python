def apply_discount(price, discount=0.05):
    discounted = price * (1 -discount)
    return discounted

def apply_tax(discounted, tax=0.07):
    taxed = discounted * (1 + tax)
    return taxed

def calculate_total(price, discount=0.05, tax=0.07):

    discounted = apply_discount(price, discount)
    final = apply_tax(discounted, tax)
    return final

total_default = calculate_total(120)
total_custom = calculate_total(100, discount=0.10, tax=0.08)
print(f"Total cost with default discount and tax: ${total_default}")
print(f"Total cost with custom discount and tax: ${total_custom}")



