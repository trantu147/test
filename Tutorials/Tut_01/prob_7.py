purchase = float(input("Please enter the amount of a purchase: $"))
state_tax = purchase*0.05
county_tax = purchase*0.025
total_tax = state_tax+county_tax
total_ofsale = purchase+total_tax
print("The amount of the purchase: $", format(purchase, ',.2f'))
print("The amount of the state sale tax: $", format(state_tax, ',.2f'))
print("The amount of the countr\y sale tax: $", format(county_tax, ',.2f'))
print("The amount of the total sale tax: $", format(total_tax, ',.2f'))
print("The amount of the total of sale: $", format(total_ofsale, ',.2f'))