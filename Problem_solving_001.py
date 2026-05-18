## #Q.1 You are making a billing system for a grocery store.
## The store has a dictionary of items with their prices.
## Write a function calculate_bill(cart, price_list) that:
## • Takes a cart (list of items),
## • Calculates and returns the total bill.




# def calculate_bill(cart,price_list):
#     total=0
#     for item in cart:
#         if item in price_list:
#             total += price_list[item]
#             ###3#sum=sum+price_list[item]
#     return total        


# price_list = {
#     "milk":50,
#     "bread":30,
#     "butter":90,
#     "eggs":60
# }

# cart = ["milk","bread","eggs","milk"]

# total_bill = calculate_bill(cart, price_list)
# print(f"Total grocery bill: rs{total_bill} ")







##### Question 2: Student Marks Record
## You are managing marks of students in a class.
## Write a function find_topper (marks)
## that:
## • Takes a dictionary where keys are student names and values are marks,
## • Returns the name of the student with the highest marks.

marks = {
    "Ananya":92,
    "Rohit":88,
    "Megha":95,
    "Arjun":89

}

def find_topper(marks):
    topper_name = ''
    topper_marks = 0
    for k, v in marks.items():
        if v>topper_marks:
            topper_name = k
            topper_marks = v

    return topper_name

top_1 = print(find_topper ( marks))        
print (top_1)
        
