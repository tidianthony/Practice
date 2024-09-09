# Greetings.
greetings = "Hello!, hope you are having a good day."
print(greetings)

# Playing with variables, input and casting.
print("Playing with variables, input and casting: ")
name = input("What is your name? ")
age = input("How old are you? ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")
print(f"This is {name} and she is {age} years old. she lives at house number {house_number} on {street_name}")

# Declearing variables.
num_1 = 99, 23
num_2 = 23
num_3 = 150
string_1 = "100"

''' Cating the variables as follows:
num_1 into an string
num_2 into a float
num_3 into a string
string_1 into an integer '''

num_1 = str(num_1)
num_2 = float(num_2)
num_3 = str(num_3)
string_1 = int(string_1)

# Printing the variables according to their cast type.
print(" Declearing variables and Printing the variables according to their caTst type :")
print(type(num_1))
print(type(num_2))
print(type(num_3))
print(type(string_1))

# Basic calculations.
print("Basic calculations:")
x = 5
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
a = 13
b = 7
c = 5
result = (a + c * b + c - a)
print(f"Answer: {result}")

# Finding the sum and product of 12 and 5.
print("Finding the sum and product: ")
a = 12
b = 5
sum = (a + b)
product = (a * b)
remainder = (a / b)
print(f"sum is: {sum}")
print(f"product is: {product}")
print(f"remendir is {remainder}")

# Building a basic calculator.
print("Calculator.")
num1 = input("Enter a number")
num2 = input("Enter a number")
answer = float(num1) + float(num2)
print(f"Your answer is: {answer}")

# Mad libs game.
print("Let's play mad libs!")
colour = input("What is yout favourite colour? ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Who is your favourite celebrity? ")
print(f"Roses are {colour}")
print(f"{plural_noun} are blue")
print(f"I love {celebrity}")
