amount = 1200
tax = amount * 0.18
total = amount + tax
print(total)

if total > 1000:
    discount = total * 0.10
    total -= discount
print(tax)    
print(discount)
print(total)

age = 35
Student = "yes"

if age >= 35 or Student == 'yes':
    print("disconut available")
else:
    print("no discount")