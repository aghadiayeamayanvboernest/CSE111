print()
from datetime import datetime

shop_sales_tax_rate = .10
Sales_tax_rate = .06 

subtotal = float(input("Enter your sub total: "))

current_date_and_time = datetime.now()
weekday = current_date_and_time.weekday()

if subtotal >= 50 and (weekday==1 or weekday==2 ):
    discount = round(subtotal * shop_sales_tax_rate, 1)
    print (f"the discount amount is: {discount:.1f}")

    subtotal -= discount

sales_tax = round(subtotal * Sales_tax_rate, 1)
print(f"the sale amount is: {sales_tax:.1f}")   

total = subtotal + sales_tax
print(f"Your total amount is: {total:.1f}")
