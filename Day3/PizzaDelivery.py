print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

bill_amount = 0
if size == 'S':
    bill_amount+= 15
elif size == 'M':
    bill_amount += 20
elif size == 'L':
    bill_amount+= 25
else:
    print("Please select option S, M or L")

if pepperoni == 'Y':
    if size == 'S':
        bill_amount += 2
    else:
        bill_amount += 3

if extra_cheese == 'Y':
    bill_amount += 1

print(f"The total bill amount is : ${bill_amount}")