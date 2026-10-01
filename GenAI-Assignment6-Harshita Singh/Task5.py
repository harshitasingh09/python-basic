cart = []

while True:
    user_input = input("Enter price (or 'q' to quit): ").strip()
    
    if user_input.lower() == 'q':
        break
    
    try:
        price = float(user_input)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        cart.append(price)
    except ValueError as e:
        print(f"Error: {e}")

print(f"\nTotal items: {len(cart)}")
print(f"Total bill: {sum(cart)}")