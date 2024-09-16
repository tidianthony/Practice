'''A program that asks the user to guess a secret number between 1 and 20.
   The program gives feedback if the guess is too low or too high.
   The user has unlimited attempts until they guess the correct number.'''

# The guess number is 15
guess = None
secret_number = 15

# Using while loop and if, elif and else statments
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret_number:
        print("Your guess is too low. Try again.")
    elif guess > secret_number:
        print("Your guess is too high. Try again.")
    else:
        print("Well done! You've guessed my number.")

'''A program that continuously asks the user to enter numbers.
   The program will add the numbers entered.
   When the user enters 0, the program will stop asking for input and display the total sum.'''

# Initialzie the total sum
total_sum = 0

#Starting the while loop
while True:
    # Asking the user to enter a number
    number = int(input("Enter a number(or 0 to stop): "))

    # If the user enters 0, exit loop
    if number == 0:
        break

    # Add the number to the total sum
    total_sum + number

    # Display the total sum
    print(f"The total sum of numbers is: {total_sum}")

'''A program that continously asks the user to input a word, and the program should output the word     reversed.
   The user can stop the program by entering the word "stop".
   The program is case-insensitive.'''

# starting the while loop
while True:
    # Asking user to enter a word
    word = input("Enter a word (or stop to end): ")

    # Check if the user entered "stop" (case-insensertive)
    if word.lower == "stop":
        print("Program ended.")
        break

    # Reverse the word
    reversed_word = word[::-1]
    print(F"Reversed word: {reversed_word}")

'''Using for loop the program prints the multiplication table 1 to 12 for a number entered by the user.'''

# Asking user to enter a number
number = int(input("Enter a number: "))

# using a for loop to print the multiplication table from 1 to 12
for i in range(1,13):
    # Format the output using a f-string
    print(f"{number} * {i} = {number * i}")

'''A program that calculates the sum of all even numbers between 1 and a number entered by the user.
   The program should only sum even numbers and display the final result.'''

# Asking user to enter a number
number = int(input("Enter a number: "))

# Initializing the sum variable
sum_of_even = 0

# using a for loop to interare through numbers from 1 to the enterd number
for i in range(1, number + 1):
    #Check if the number is even
    if i % 2 ==0:
        sum_of_even += i

# Displaying the result
print(f"The sum of even numbers between 1 and {number} is: {sum_of_even}")

'''The program performs a countdown from a number entered bt the user to 0.
   After each number, it displays a massage like BOOm! when the countdown reaches 0.'''

# Asking the user to enter a starting number for the countdown
satrt_number = int(input("Enter the countdown starting number: "))

# Using a for loop to countdown from the number entered to number 0
for i in range(secret_number,-1,-1):
    if i > 0:
        print(i)
    else:
        print("BOOM!!!")