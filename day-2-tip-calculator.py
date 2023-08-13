print("Hello! Welcome to your tip calculator!")

total_bill = float(input("How much was the total bill? $"))

tip = int(input("What percentage of tip would you like to give for the service? Enter a number! "))

total_tip = (tip + 100)/100

person = int(input("How many people to split the bill? "))

result = str(round((total_bill / person) * total_tip, 2))

print("Each person should pay $" + result)
