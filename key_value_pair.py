# # Disctionary or key value pair
# # A dictionary is a collection that is changeable and does not allow dublicates.
# # syntax

# # EXAMPLE 1 

# my_personal_dict={ "red":"football", "green":"football",}

# # EXAMPLE 2
# # KEY IS OF INTEGER TYPE.
# Aadil = {1:"hello" , 2:"world"}

# print(Aadil)


# my_dict = {"Name":"Aadil", 2:[45,4,6,7,7,77,7]}
# print(my_dict[2][4])


# employee = {
#     'name':["aadil","aasif","aamir"],
#     'age':[21,20,22],
#     'income':[90,89,91]
# }

# print(employee['name'][0],employee['age'][0],employee['income'][0])



#QUESTIONS 
# CREATE A DICTONARY OF 3 STUDENTS WITH MARKS AND PRINT THE TOPPER

students = {
    "A":88,
    "B":95,
    "C":82
}

#APPROACH 1

# if students ["A"] > students ["B"] and students ["A"] > students ["C"]:
#     print("The topper is A")
# elif students ["B"] > students ["A"] and students ["B"] > students ["C"]:
#     print ("The topper is B")
# elif students ["C"] > students ["A"] and students ["C"] > students ["B" ]:
#     print ("The topper is C")
# else:
#     print("All have same marks")



# APPROACH 2

topper = ""
highest_marks = -1

for name, marks in students. items ():
    if marks > highest_marks:
        highest_marks = marks
        topper = name

print(f"The topper is {topper} with {highest_marks} marks.")      

# THE f IA KNOWN AS F STRING

print("The topper is" , topper,"with",highest_marks, "marks.")