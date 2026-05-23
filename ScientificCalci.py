# # Scientific Calculator in Python

# import math

# print("=== Scientific Calculator ===")
# print("Operations:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")
# print("5. Power (^)")
# print("6. Square Root")
# print("7. Sine")
# print("8. Cosine")
# print("9. Tangent")
# print("10. Logarithm")
# print("11. Factorial")

# choice = int(input("\nEnter your choice (1-11): "))

# if choice == 1:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result =", a + b)

# elif choice == 2:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result =", a - b)

# elif choice == 3:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print("Result =", a * b)

# elif choice == 4:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
    
#     if b != 0:
#         print("Result =", a / b)
#     else:
#         print("Division by zero is not allowed")

# elif choice == 5:
#     a = float(input("Enter base number: "))
#     b = float(input("Enter power: "))
#     print("Result =", a ** b)

# elif choice == 6:
#     a = float(input("Enter number: "))
#     print("Result =", math.sqrt(a))

# elif choice == 7:
#     angle = float(input("Enter angle in degrees: "))
#     print("Result =", math.sin(math.radians(angle)))

# elif choice == 8:
#     angle = float(input("Enter angle in degrees: "))
#     print("Result =", math.cos(math.radians(angle)))

# elif choice == 9:
#     angle = float(input("Enter angle in degrees: "))
#     print("Result =", math.tan(math.radians(angle)))

# elif choice == 10:
#     a = float(input("Enter number: "))
#     print("Result =", math.log10(a))

# elif choice == 11:
#     a = int(input("Enter number: "))
#     print("Result =", math.factorial(a))

# else:
#     print("Invalid Choice")

# Improved Scientific Calculator





import math

print("=== Scientific Calculator ===")

while True:

    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")
    print("12. Exit")

    choice = input("Enter choice (1-12): ")

    if choice == "12":
        print("Calculator Closed")
        break

    # Operations needing two numbers
    if choice in ["1", "2", "3", "4", "5"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", a + b)

        elif choice == "2":
            print("Result =", a - b)

        elif choice == "3":
            print("Result =", a * b)

        elif choice == "4":
            if b != 0:
                print("Result =", a / b)
            else:
                print("Error: Cannot divide by zero")

        elif choice == "5":
            print("Result =", a ** b)

    # Square Root
    elif choice == "6":
        a = float(input("Enter number: "))

        if a >= 0:
            print("Result =", math.sqrt(a))
        else:
            print("Error: Negative number")

    # Trigonometric Functions
    elif choice in ["7", "8", "9"]:
        angle = float(input("Enter angle in degrees: "))

        if choice == "7":
            print("Result =", math.sin(math.radians(angle)))

        elif choice == "8":
            print("Result =", math.cos(math.radians(angle)))

        elif choice == "9":
            print("Result =", math.tan(math.radians(angle)))

    # Logarithm
    elif choice == "10":
        a = float(input("Enter number: "))

        if a > 0:
            print("Result =", math.log10(a))
        else:
            print("Error: Log undefined")

    # Factorial
    elif choice == "11":
        a = int(input("Enter integer: "))

        if a >= 0:
            print("Result =", math.factorial(a))
        else:
            print("Error: Factorial undefined")

    else:
        print("Invalid Choice")