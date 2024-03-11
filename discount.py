def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price
    
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)
if final_price != original_price:
    print(f"The final price after applying the discount is ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is ${original_price:.2f}")