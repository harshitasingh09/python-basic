prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
    try:
        # Comparison with int raises TypeError if price is not a number
        if price < 0:
            raise ValueError("Negative price not allowed")
        total += price
    except TypeError:
        print(f"Skipped '{price}': Invalid type (not a number).")
    except ValueError as e:
        print(f"Skipped '{price}': {e}.")
    
    print(f"Running total: {total}")

print(f"\nFinal Bill Total: {total}")