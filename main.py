"""Integration Project"""
# Nash Morrison
# A Built-Over-Time Mini-Game to help solidify the material in my head.
# COP 1500 Professor Brown
import numpy as np


def cube(i):

    """Function to Cube"""

    it = np.nditer([i, None])
    for a, b in it:
        b[...] = a * a * a
    return it.operands[1]


print("Hello!, and welcome to Marty's Magical Carnival!")
name = input("\nWhat is your name?")
for x in range(1):
    print("\nHello,", name, "and welcome!\n", sep='  ')  # Using an sep==.


def greet():
    """A function for a simple greet"""

    print("Hello again, " + name, "!")


print("Let us first buy you a ticket!\n",
      "\nDepending on your age depends on how much your ticket costs.\n",
      "\n-Ages 25 and under and 65 and over - Free!!!",
      "\n-Ages 26 - 64 costs $1!",
      "\n-Ages 9 and under are not allowed in\n")

try:
    age = int(input("How old are you?: "))

    while age >= 10:
        print("\nYou are old enough to enter the carnival!")
        if age <= 25 or age >= 65:
            print("\nYour ticket is free!")
            break
        elif age > 25 or age < 65:
            print("\nYour ticket is 1$.")
            break

    else:
        print("\nYou are not old enough"
              "\nDon't tell anyone, it will be our little secret :) ")
except ValueError:
    print(
        "That is not a number, but if you want to be sneaky that is cool too.")

#  This chain of if/elif nested statements is just to showcase all the layers.
print("\nTo be allowed inside my carnival, ",
      "you must first solve a handful of math problems!")

answer = input("\nWould you like to play? " "Type Yes or yes:  ")

if answer == "Yes":
    print("Okay, Awesome!")
elif answer == "yes":
    print("Okay, Awesome!")

elif answer == "No":
    print("Are you sure? Type Yes or yes ")
    answer = input()

    if answer == "Yes":
        print("Okay, Awesome!")
    elif answer == "yes":
        print("Okay, Awesome!")

    elif answer == "No":
        print("Are you sure? Type Yes or yes ")
        answer = input()

        if answer == "Yes":
            print("Okay, Awesome!")
        elif answer == "yes":
            print("Okay, Awesome!")
        else:
            print("Carefully read the directions given to you, trickster.")

    elif answer == "no":
        print("Are you sure? Type Yes or yes ")
        answer = input()

        if answer == "Yes":
            print("Okay, Awesome!")
        elif answer == "yes":
            print("Okay, Awesome!")
        else:
            print("Carefully read the directions given to you, trickster.")

elif answer == "no":
    print("Are you sure? Type Yes or Yes ")
    answer = input()

    if answer == "Yes":
        print("Okay, Awesome!")
    elif answer == "yes":
        print("Okay, Awesome!")

    elif answer == "No":
        print("Are you sure? Type Yes or yes ")
        answer1 = input()

        if answer == "Yes":
            print("Okay, Awesome!")
        elif answer == "yes":
            print("Okay, Awesome!")
        else:
            print("Carefully read the directions given to you, trickster.")

    elif answer == "no":
        print("Are you sure? Type Yes or yes ")
        answer = input()

        if answer == "Yes":
            print("Okay, Awesome!")
        elif answer == "yes":
            print("Okay, Awesome!")
        else:
            print("Carefully read the directions given to you, trickster.")
else:
    print("Carefully read the directions given to you, trickster.")


# First math problem adds together stored variables and outputs the answer 4.
num0, num1, num2, num3, num4 = 1, 2, 3, 4, 5
print("\nQuestion 1:",
      "\nWhat is 3 + 1?",
      "(Type the appropriate uppercase letter):")

# Answer is the variable for 4.
answer = input("A: 2 B: 3 C: 4 D: 5 ")

while answer != "C":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 2 B: 3 C: 4 D: 5")
    answer = input()

# Using the Addition Operator.
print(num0 + num2,
      "\nYes!, the correct answer is C, 4!")

# Second math problem multiplies together
# stored variables and outputs the answer 6.
num1, num2, num3, num4 = -2, 3, 4, 6
print("\nQuestion 2:",
      "\nWhat is 3 x 2?"
      "(Type the appropriate uppercase letter):")
answer = input("A: 2 B: 4 C: 8 D: 6 ")

while answer != "D":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 2 B: 4 C: 8 D: 6")
    answer = input()

# Using the Multiplication Operator.
# Testing the pre-built "abs" function.
print(abs(-6),
      "\nYes!, the correct answer is D, 6!")

# Third math problem uses exponentiation for two stored variables.
num1, num2, num3, = 2, 3, 8
print("\nQuestion 3:",
      "\nWhat is 2 to the power of 3?"
      "(Type the appropriate uppercase letter):")
answer = input("A: 8 B: 6 C: 5 D: 1 ")

while answer != "A":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 8 B: 6 C: 5 D: 1")
    answer = input()

# Using the Exponentiation Operator.
# Using my cube function that allows a parameter.
print(cube(2),
      "\nYes!, the correct is A, 8!")

# Fourth math problem divides two stored variables and outputs the answer 4.
num1, num2 = 4, 16
print("\nQuestion 4:",
      "\nWhat is 16 divided by 4?"
      "(Type the appropriate uppercase letter):")
answer = input("A: 4 B: 8 C: 12 D: 16 ")

while answer != "A":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 4 B: 8 C: 12 D: 16")
    answer = input()

# Using the Division Operator.
print(int(num2 / num1),
      "\nYes! The correct answer is A, 4!")

# Fifth math problem looks for the remainder of two numbers.
num1, num2 = 5, 26
print("\nQuestion 5:",
      "\nWhat is the remainder of 26 divided by 5?"
      "(Type the appropriate uppercase letter):")
answer = input("A: 2 B: 1 C: 3 D: 4 ")

while answer != "B":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 2 B: 1 C: 3 D: 4")
    answer = input()

# Using the Modulus Operator.
print(num2 % num1,
      "\nYes! The correct answer is B, 1!")

# Sixth math problem deals with floor division.
# Looking for the number rounded down to the nearest whole number.
num1, num2 = 7, 15
print("\nQuestion 6:",
      "\nWhat is 15 divided by 7 rounded "
      "down to the nearest whole number?"
      "(Type the appropriate uppercase letter):")
answer = input("A: 2 B: 6 C: 5 D: 8 ")

while answer != "A":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 2 B: 6 C: 5 D: 8")
    answer = input()

# Using the Floor Division Operator to output our answer.
# We are using a float assignment just as an example to output a float number.
print((float(num2 // num1)),
      "\nYes!, the correct answer is A, 2!")

# Seventh math problem deals with subtracting two variables.
num1, num2 = 3, 4
print("\nQuestion 7:",
      "\nWhat is 4 - 3?"
      "(Type the appropriate uppercase letter):")
answer = input("A: 7 B: 1 C: 12 D: 10 ")

while answer != "B":
    print("\nThat is the incorrect answer, please try again.",
          "\nA: 7 B: 1 C: 12 D: 10")
    answer = input()

# Using the Subtraction Operator
# to output our answer.
print(num2 - num1,
      "\nYes! the correct answer is B, 1!")

# Eighth math problem looks to see if 2 values are equal to one another.
x, y, z = 4, 5, 4
print("\nQuestion 8:",
      "X = 4, Y = 5, Z = 4",
      "\nDoes X equal Z?"
      "(Type the appropriate uppercase letter): ")
answer = input("A: Yes   B: No ")

if answer == "A":
    print(x and z,
          "\nYes! They are equal to each other!")

elif answer == "a":
    print(x and z,
          "\nYes! They are equal to each other!")


elif answer == "B":
    print("\nSorry, that is incorrect, please try again.",
          "\nA: Yes   B: No")
    answer = input()

    if answer == "A":
        print(x and z,
              "\nYes! They are equal to each other!")

    elif answer == "a":
        print(x and z,
              "\nYes! They are equal to each other!")


elif answer == "b":
    print("\nSorry, that is incorrect, please try again.",
          "\nA: Yes   B: No")
    answer = input()

    if answer == "A":
        print(x and z,
              "\nYes! They are equal to each other!")

    elif answer == "a":
        print(x and z,
              "\nYes! They are equal to each other!")

else:
    print("\nNone of these match at all, but the answer is yes.")

#  Ninth math problems looks to see if 2 values are not equal to each other.
print("\nQuestion 9:",
      "\nX = 4, Y = 5, Z = 4",
      "\nDoes X equal Y"
      "\n(Type the appropriate uppercase letter): ")
answer = input("A: Yes   B: No ")

if answer == "B":
    print(not x == y,
          "\nYes! They are not equal to each other.")


elif answer == "b":
    print(not x == y,
          "\nYes! They are not equal to each other.")


elif answer == "A":
    print("\nSorry, that is incorrect, please try again.",
          "\nA: Yes   B: No")
    answer = input()

    if answer == "B":
        print(not x == y,
              "\nYes! They are not equal to each other.")

    elif answer == "b":
        print(not x == y,
              "\nYes! They are not equal to each other.")


elif answer == "a":
    print("\nSorry, that is incorrect, please try again.",
          "\nA: Yes   B: No")
    answer = input()

    if answer == "B":
        print(not x == y,
              "\nYes! They are not equal to each other.")

    elif answer == "b":
        print(not x == y,
              "\nYes! They are not equal to each other.")

else:
    print("That is not a correct response, but the answer is Yes.")

# Tenth math problem deals with a for statement and seeing if a variable is
# greater than y or 5.
x, y, z = 4, 5, 6
print("\nQuestion 10:",
      "X = 4, Y = 5, Z = 6",
      "\nIs X Greater than Y or is Z Greater than Y?\n"
      "\nA: X is Greater   B: Z is Greater:\n"
      "\n(Type the appropriate uppercase letter):")
answer = input("A: Yes   B: No ")

if answer == "B":
    print(x > y or z,
          "\nYes! 6 is greater than 5!")


elif answer == "b":
    print(x > y or z,
          "\nYes! 6 is greater than 5!")


elif answer == "A":
    print("\nSorry, that is incorrect, please try again.\n"
          "\nIs X Greater than Y or is Z Greater than Y?\n"
          "\nA: Yes   B: No")
    answer = input()

    if answer == "B":
        print(x > y or z,
              "\nYes! 6 is greater than 5!")

    elif answer == "b":
        print(x > y or z,
              "\nYes! 6 is greater than 5!")

elif answer == "a":
    print("\nSorry, that is incorrect, please try again.\n"
          "\nIs X Greater than Y or is Z Greater than Y?\n"
          "\nA: Yes   B: No")
    answer = input()

    if answer == "B":
        print(x > y or z,
              "\nYes! 6 is greater than 5!")

    elif answer == "b":
        print(x > y or z,
              "\nYes! 6 is greater than 5!")

else:
    print("That is not a correct response, but the answer is Yes.")

# The math portion of the game is over.
print("\nCongratulations on passing all of the math questions! "
      "You really are a bright cookie!\n"
      "\nNow I am going to say a word associated with the carnival "
      "and you are going to fill in the blank.\n",
      end='      ')  # Using an end='' funct.

word1, word2 = "Cotton", "Candy"
answer = input("When I say Cotton, you think of?"
               "(Type your answer starting with an uppercase letter):")

while answer != "Candy":
    print("\nNo, that's not it. Try again.",
          "\nWhen I say cotton, say?")
    answer = input()

# Using the Addition operator to concatenate two words.
# Using the Multiplication Operator on one word.
print(word1 + word2,
      "\nYay! " * 3, "\nYou guessed correctly!\n")

greet()

print("Thank you for playing!")
