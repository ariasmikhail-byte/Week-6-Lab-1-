# Mikhail Arias 
# CMP - 131
# Week 6
# Software Discount Program
# Lab 1

units_purchased = int(input("Enter the number of software units purchased:"))
Original_cost = units_purchased * 99.00
print("The Origianl Cost is: $", +Original_cost)
if units_purchased <= 0:
    print("Error: The number of units must be greater than zero.")
else:
    if units_purchased < 10:
        discount_rate = 0
    elif units_purchased < 20:
        discount_rate = 0.20
    elif units_purchased < 50:
        discount_rate = 0.30
    elif units_purchased < 100:
        discount_rate = 0.40
    else:
        discount_rate = 0.50

    # Calculate the original cost, discount, and final cost.
    price_per_unit = 99.00
    original_cost = units_purchased * price_per_unit
    discount_amount = original_cost * discount_rate
    final_cost = original_cost - discount_amount
    print("------- Purchase Report -------")
    print(f"Units purchased: {units_purchased}")
    print(f"Price per unit: ${price_per_unit:,.2f}")
    print(f"Original cost: ${original_cost:,.2f}")
    print(f"Discount percentage: {discount_rate:.0%}")
    print(f"Discount amount: ${discount_amount:,.2f}")
    print(f"Final purchase cost: ${final_cost:,.2f}")
