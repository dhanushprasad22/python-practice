name = input("enterur name:")
age = int(input("Enter your age: "))  # Convert input to integer
amount = 6000
tax = amount * 0.18  # 18% tax
total = amount + tax
print(total)
if age >= 33:
    discount = total - tax
    print("Discounted amount:", discount)
    print(f"Respected {name}, you have a discount.")
else:
    print(f"Respected {name}, you have no discount.")

