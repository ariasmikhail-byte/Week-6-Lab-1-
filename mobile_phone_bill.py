# Mikhail Arias 
# CMP - 131
# Week 6
# Mobile Phone bill
# Lab 1

print("======== Mobile Phone Service Bill ========")
print("A: $39.99 monthly, 450 minutes, $0.45 per extra minute")
print("B: $59.99 monthly, 900 minutes, $0.40 per extra minute")
print("C: $69.99 monthly, unlimited minutes, $0.00 per extra minute")

# Ask for the package and minutes used.
package = input("Enter your package (A, B, or C): ")
minutes_used = int(input("Enter the number of minutes used: "))

# Validate the package and minutes.

if package != "A" and package != "B" and package != "C":
    print("Error: Invalid package. Please select A, B, or C.")
elif minutes_used < 0:
    print("Error: Minutes used must be zero or greater.")
else:
    additional_minutes = 0
    additional_charge = 0.00
 # Determine the monthly charge and calculate extra charges.
    if package == "A":
        monthly_charge = 39.99
        if minutes_used > 450:
            additional_minutes = minutes_used - 450
            additional_charge = additional_minutes * 0.45
    elif package == "B":
        monthly_charge = 59.99
        if minutes_used > 900:
            additional_minutes = minutes_used - 900
            additional_charge = additional_minutes * 0.40
    else:
        monthly_charge = 69.99

# Calculate the total bill.
    total_bill = monthly_charge + additional_charge

    # Display the monthly bill.
    print("------- Monthly Bill -------")
    print(f"Selected package: {package}")
    print(f"Minutes used: {minutes_used}")
    if package == "C":
        print("Included minutes: Unlimited")
    print(f"Monthly package charge: ${monthly_charge:.2f}")
    print(f"Additional minutes: {additional_minutes}")
    print(f"Additional-minute charge: ${additional_charge:.2f}")
    print(f"Total amount due: ${total_bill:.2f}")
