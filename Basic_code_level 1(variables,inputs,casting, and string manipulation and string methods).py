# Welcome to the Fun Interactive Story Generator

# Collect various user inputs

# String inputs
user_name = input("Enter your name: ")
friend_name = input("Enter your friend's name: ")
favorite_food = input("Enter your favorite food: ")
favorite_place = input("Enter your favorite place: ")

# Integer inputs
age = input("Enter your age: ")
lucky_number = input("Enter your lucky number: ")

# Float input
distance_travelled = input("Enter how many kilometers you traveled last week (use a decimal): ")

# More inputs for fun interaction
pet_name = input("Enter your pet's name (if you don't have one, make one up!): ")
dream_car = input("Enter your dream car: ")

# Type casting and conversions

# Casting age to integer
age = int(age)

# Casting lucky number to float
lucky_number_float = float(lucky_number)

# Casting distance to float for manipulation
distance_travelled = float(distance_travelled)

# Convert lucky number to string for later story
lucky_number_str = str(lucky_number)

# Perform basic arithmetic calculations

# Let's have some fun with numbers
number1 = float(input("Enter a random number (this will be part of the fun calculations!): "))
number2 = float(input("Enter another random number: "))

# Basic arithmetic operations
sum_result = number1 + number2
subtraction_result = number1 - number2
multiplication_result = number1 * number2
division_result = number1 / number2  # Division, no error handling for introduction purposes

# Story-driven casting and manipulated numbers
lucky_number_multiplied = int(lucky_number) * 3
age_and_lucky_number_sum = age + lucky_number_float

# Generate the creative story using all these inputs and calculations

story = (f"""
Here's a fun story about {user_name.upper()} and their amazing adventures!

One fine day, {user_name} and {friend_name.lower()}, best friends since childhood, decided to set out for a journey. 
The plan was to visit their favorite place, {favorite_place}, where they would feast on {favorite_food}. But they also decided to solve a few math problems along the way!

First, {user_name} and {friend_name} added {number1} and {number2} and got {sum_result:.2f}. Math win! 
Then, they subtracted {number2} from {number1} and got {subtraction_result:.2f}. Not bad at all.

Feeling brave, they tried multiplying {number1} and {number2} and got {multiplication_result:.2f}. Quite the powerful result!

And when {number1} was divided by {number2}, the result was {division_result:.2f}. Basic math, right?

On their way to {favorite_place}, they covered a distance of {distance_travelled} kilometers, but decided to round it to {int(distance_travelled)} kilometers, just for fun.

To keep the trip exciting, they brought along their pet {pet_name} and drove in {user_name}'s dream car—a {dream_car}. 
They also joked about {user_name}'s age—turning {age} soon—and how they added their lucky number ({lucky_number}) to it, which gave them a grand total of {age_and_lucky_number_sum:.2f}. Now that's some math magic!

They tripled their lucky number just for fun and got {lucky_number_multiplied}. With that lucky number in mind, they felt invincible.

In the end, the math-filled road trip turned out to be the best adventure ever. The moral of the story? 
Math makes every journey more fun!

{user_name.upper()}, {friend_name.lower()}, and {pet_name} had a blast driving through life with {dream_car}, 
a calculator in hand, and plenty of laughs from all the funny calculations!
""")

# Display the story to the user
print("\nHere is your story:")
print(story)

# Closing message
print("\nThanks for playing the Fun Interactive Story Generator!")