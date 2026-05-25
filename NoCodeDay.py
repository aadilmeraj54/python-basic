# # # Scientific Calculator in Python

# # import math

# # print("=== Scientific Calculator ===")
# # print("Operations:")
# # print("1. Addition (+)")
# # print("2. Subtraction (-)")
# # print("3. Multiplication (*)")
# # print("4. Division (/)")
# # print("5. Power (^)")
# # print("6. Square Root")
# # print("7. Sine")
# # print("8. Cosine")
# # print("9. Tangent")
# # print("10. Logarithm")
# # print("11. Factorial")

# # choice = int(input("\nEnter your choice (1-11): "))

# # if choice == 1:
# #     a = float(input("Enter first number: "))
# #     b = float(input("Enter second number: "))
# #     print("Result =", a + b)

# # elif choice == 2:
# #     a = float(input("Enter first number: "))
# #     b = float(input("Enter second number: "))
# #     print("Result =", a - b)

# # elif choice == 3:
# #     a = float(input("Enter first number: "))
# #     b = float(input("Enter second number: "))
# #     print("Result =", a * b)

# # elif choice == 4:
# #     a = float(input("Enter first number: "))
# #     b = float(input("Enter second number: "))
    
# #     if b != 0:
# #         print("Result =", a / b)
# #     else:
# #         print("Division by zero is not allowed")

# # elif choice == 5:
# #     a = float(input("Enter base number: "))
# #     b = float(input("Enter power: "))
# #     print("Result =", a ** b)

# # elif choice == 6:
# #     a = float(input("Enter number: "))
# #     print("Result =", math.sqrt(a))

# # elif choice == 7:
# #     angle = float(input("Enter angle in degrees: "))
# #     print("Result =", math.sin(math.radians(angle)))

# # elif choice == 8:
# #     angle = float(input("Enter angle in degrees: "))
# #     print("Result =", math.cos(math.radians(angle)))

# # elif choice == 9:
# #     angle = float(input("Enter angle in degrees: "))
# #     print("Result =", math.tan(math.radians(angle)))

# # elif choice == 10:
# #     a = float(input("Enter number: "))
# #     print("Result =", math.log10(a))

# # elif choice == 11:
# #     a = int(input("Enter number: "))
# #     print("Result =", math.factorial(a))

# # else:
# #     print("Invalid Choice")

# # Improved Scientific Calculator





# import math

# print("=== Scientific Calculator ===")

# while True:

#     print("\nChoose Operation:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Power")
#     print("6. Square Root")
#     print("7. Sine")
#     print("8. Cosine")
#     print("9. Tangent")
#     print("10. Logarithm")
#     print("11. Factorial")
#     print("12. Exit")

#     choice = input("Enter choice (1-12): ")

#     if choice == "12":
#         print("Calculator Closed")
#         break

#     # Operations needing two numbers
#     if choice in ["1", "2", "3", "4", "5"]:
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))

#         if choice == "1":
#             print("Result =", a + b)

#         elif choice == "2":
#             print("Result =", a - b)

#         elif choice == "3":
#             print("Result =", a * b)

#         elif choice == "4":
#             if b != 0:
#                 print("Result =", a / b)
#             else:
#                 print("Error: Cannot divide by zero")

#         elif choice == "5":
#             print("Result =", a ** b)

#     # Square Root
#     elif choice == "6":
#         a = float(input("Enter number: "))

#         if a >= 0:
#             print("Result =", math.sqrt(a))
#         else:
#             print("Error: Negative number")

#     # Trigonometric Functions
#     elif choice in ["7", "8", "9"]:
#         angle = float(input("Enter angle in degrees: "))

#         if choice == "7":
#             print("Result =", math.sin(math.radians(angle)))

#         elif choice == "8":
#             print("Result =", math.cos(math.radians(angle)))

#         elif choice == "9":
#             print("Result =", math.tan(math.radians(angle)))

#     # Logarithm
#     elif choice == "10":
#         a = float(input("Enter number: "))

#         if a > 0:
#             print("Result =", math.log10(a))
#         else:
#             print("Error: Log undefined")

#     # Factorial
#     elif choice == "11":
#         a = int(input("Enter integer: "))

#         if a >= 0:
#             print("Result =", math.factorial(a))
#         else:
#             print("Error: Factorial undefined")

#     else:
#         print("Invalid Choice")


        

# for i in range(1, 5):
#     print("Hello, World!")
# print("Done")

# name = "Alice"
# age = 20
# print(name)
# print(age)

# a = 10
# b = 5
# sum = a + b
# print(sum)

# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)
# print("Finished")


# import random

# secret_number = random.randint(1, 10)

# print("Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 10")

# while True:
#     guess = int(input("Enter your guess: "))

#     if guess == secret_number:
#         print("🎉 Correct! You guessed the number.")
#         break
#     elif guess < secret_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")

# import random
# import string

# # Ask user for password length
# length = int(input("Enter password length: "))

# # Characters to use
# characters = string.ascii_letters + string.digits + string.punctuation

# # Generate password
# password = ''.join(random.choice(characters) for _ in range(length))

# print("\nGenerated Password:")
# print(password)

# import pygame
# import random
# import sys

# # Initialize pygame
# pygame.init()

# # Screen size
# WIDTH = 600
# HEIGHT = 400
# BLOCK = 20

# # Colors
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# WHITE = (255, 255, 255)

# # Create screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snake Game")

# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 25)

# # Snake settings
# snake = [(100, 100)]
# snake_dir = (BLOCK, 0)

# # Food
# food = (
#     random.randrange(0, WIDTH, BLOCK),
#     random.randrange(0, HEIGHT, BLOCK)
# )

# score = 0

# def draw_snake(snake):
#     for segment in snake:
#         pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

# def draw_food(food):
#     pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))

# def show_score(score):
#     text = font.render(f"Score: {score}", True, WHITE)
#     screen.blit(text, (10, 10))

# # Game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and snake_dir != (0, BLOCK):
#                 snake_dir = (0, -BLOCK)
#             if event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK):
#                 snake_dir = (0, BLOCK)
#             if event.key == pygame.K_LEFT and snake_dir != (BLOCK, 0):
#                 snake_dir = (-BLOCK, 0)
#             if event.key == pygame.K_RIGHT and snake_dir != (-BLOCK, 0):
#                 snake_dir = (BLOCK, 0)

#     # Move snake
#     head_x = snake[0][0] + snake_dir[0]
#     head_y = snake[0][1] + snake_dir[1]
#     new_head = (head_x, head_y)

#     # Collision with wall
#     if (
#         head_x < 0 or head_x >= WIDTH or
#         head_y < 0 or head_y >= HEIGHT or
#         new_head in snake
#     ):
#         print("Game Over! Final Score:", score)
#         pygame.quit()
#         sys.exit()

#     snake.insert(0, new_head)

#     # Food collision
#     if new_head == food:
#         score += 1
#         food = (
#             random.randrange(0, WIDTH, BLOCK),
#             random.randrange(0, HEIGHT, BLOCK)
#         )
#     else:
#         snake.pop()

#     # Draw everything
#     screen.fill(BLACK)
#     draw_snake(snake)
#     draw_food(food)
#     show_score(score)

#     pygame.display.update()
#     clock.tick(10)

# import time

# text = "Python is fun and easy to learn."

# print("Typing Speed Test")
# print("------------------")
# print("Type this sentence exactly:")
# print(text)

# input("\nPress Enter when you're ready...")

# start_time = time.time()

# typed = input("\nStart typing: ")

# end_time = time.time()

# time_taken = end_time - start_time

# if typed == text:
#     words = len(text.split())
#     wpm = (words / time_taken) * 60

#     print("\n✅ Correct!")
#     print(f"Time Taken: {time_taken:.2f} seconds")
#     print(f"Typing Speed: {wpm:.2f} WPM")
# else:
#     print("\n❌ Text did not match.")


# Mini Dice Roller 🎲

# import random

# while True:
#     input("Press Enter to roll the dice...")
    
#     dice = random.randint(1, 6)
#     print("You rolled:", dice)

#     again = input("Roll again? (y/n): ").lower()

#     if again != 'y':
#         print("Thanks for playing!")
#         break

#     # Mini Countdown Timer ⏳


# import time

# seconds = int(input("Enter countdown time in seconds: "))

# while seconds > 0:
#     print("Time left:", seconds, "seconds")
#     time.sleep(1)
#     seconds -= 1

# print("⏰ Time's up!")


# Rock Paper Scissors Game ✊📄✂️

# import random

# choices = ["rock", "paper", "scissors"]

# computer = random.choice(choices)
# player = input("Choose rock, paper, or scissors: ").lower()

# print("Computer chose:", computer)

# if player == computer:
#     print("It's a tie!")
# elif (
#     (player == "rock" and computer == "scissors") or
#     (player == "paper" and computer == "rock") or
#     (player == "scissors" and computer == "paper")
# ):
#     print("🎉 You win!")
# else:
#     print("😢 You lose!")


# Mini Even or Odd Checker

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")