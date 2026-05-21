######Question: Supermarket Billing System
## A supermarket keeps track of customer purchases each day.
## Each customer can buy multiple different products, and each product has a quantity and price per unit.
## Write a program that does the following:
## • For each customer:
## • Ask for the number of products they bought.
## • For each product:
## • Ask for the product name, quantity, and price per unit.
## • Calculate the total price for that product (quantity x price).
## • After all products are entered for a customer, display:
## • The list of all products with their quantities and total prices.
## • The total bill for that customer.
## • Do this for multiple customers (e.g., until you say "no" to adding a new customer).
## Extra:
## Himanshu Sharma
## At the end, display the grand total of all customers' bills combined.



# name = input()
# print("The name that you entered into the variable name is ", name)
# print(type(name))
# age=(input())
# print("The age that you enterd into the age variable is", age)
# print(type(age))

grand_toatl = 0

while True:
    total = 0
    products = []
    num_products = int(input("Enter number of products bought: "))

    for _ in range(num_products):
        name = input ("Enter product name: ")
        quantity = int(input(f"Enter quantity of  {name}: "))
        price_per_unit = float(input(f"Enter price per unit of {name}: "))
        total_price = quantity * price_per_unit
        products.append((name, quantity, total_price))
        total += total_price

        print("Products bought")
        for name, quantity, total_price in products:
            print(f"{name} - Quantity: {quantity}, Total price: ${total_price:.2f}")

    print(f"Total bill for customer: ${total:.2f}\n")
    grand_total += total

    more = input("Add another customer? (yes/no): ")
    if more.lower() != 'yes':
        break
print (f"Grand total from all customers: {grand_total: 2f}")    
