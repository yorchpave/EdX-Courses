#Set values for maximum and minimum order variables

max_value = 100.00
min_value = 0.25

# Get order_amount input 

order_amount = input("Enter cheese order weight (numeric value): ")

# Cast order_amount to float

casted_order_amount = float(order_amount)

# Set random price
price = casted_order_amount * 7.5

# Check casted_order_amount and give message checking boundaries

if casted_order_amount > max_value:
    print(casted_order_amount,"is more than currently available stock")
elif casted_order_amount < min_value:
    print(casted_order_amount,"is below minimum order amount")
else:
    print(casted_order_amount,"costs $", price)   


