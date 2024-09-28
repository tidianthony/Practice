# Welcome to list exercises

'''Exercise 1: Create Your Own Playlist'''

# Initialize an empty playlist
playlist = ""

# Ask the user for their favorite song
song = input("What's your favorite song? ")
playlist += song + "; "  # Adding the song to the playlist

# Ask for another song
another_song = input("Enter another song: ")
playlist += another_song + "; "  # Adding the next song

# Display the playlist
print("Your Playlist: ", playlist.strip())

'''Exercise 2: Guess the Fruit'''

# Create a string of fruits
fruits = "apple, banana, cherry, date"

# Ask the user to guess a fruit
guess = input("Guess a fruit from the list (apple, banana, cherry, date): ")

# Check if the guess is correct and display the result
result = "Correct! You guessed: " + guess if guess in fruits else "Oops! That fruit is not in the list."
print(result)

'''Exercise 3: Personalize Your Snack List'''

# Start with an empty snack list
snacks = ""

# Ask the user for their favorite snack
snack = input("What's your favorite snack? ")
snacks += snack + "; "  # Adding the snack to the list

# Ask for another snack
another_snack = input("Enter another favorite snack: ")
snacks += another_snack + "; "  # Adding the next snack

# Show the personalized snack list
print("Your Snack List: ", snacks.strip())

'''Exercise 4: Dream Travel Destinations'''

# Initialize an empty destinations string
destinations = ""

# Ask the user for their dream destination
destination = input("What is your dream travel destination? ")
destinations += destination + "; "  # Adding the destination

# Ask for another destination
another_destination = input("Enter another dream destination: ")
destinations += another_destination + "; "  # Adding the next destination

# Show the dream destinations
print("Your Dream Destinations: ", destinations.strip())
