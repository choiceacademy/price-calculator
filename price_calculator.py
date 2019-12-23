import math
# Ask the user how much their meal or product costs
print("Welcome to the price calculator! We will ask you a few questions and calculate your total cost.")
original_p = float(input("How much does your meal/product cost? (Don't use the $ sign) "))
# Ask the percent tax in their location
tax_p = float(input("What is the percent tax in your location? (Don't use the % sign) "))
# Ask the percent tip that the person would like to give
tip_p = float(input("What is the percent tip you would like to give? (Don't use the % sign) "))
# Calculate the total cost 
total_p = original_p + (original_p*(tax_p/100.0)) + (original_p*(tip_p/100.0))
total_p = round(total_p,2)
print ("Your total is: $" ,total_p)
