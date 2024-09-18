import random  # Import the random module for random events

# Game introduction
print("Welcome to 'Treasure Hunt'!")
print("You are in a mysterious forest searching for hidden treasure.")
print("Make your choices wisely to find the treasure!\n")

# Game loop
while True:
    # Present the player with choices of places to explore
    print("You can go to:")
    print("1. The Cave")
    print("2. The River")
    print("3. The Old Tree")
    choice = input("Which place do you want to explore? (1, 2, or 3): ")

    # If the player chooses the Cave
    if choice == '1':
        print("\nYou enter the Cave.")
        action = input("You see a treasure chest! Do you want to 'open' it or 'leave'? ")
        if action == 'open':
            # Random chance to find treasure or get trapped
            if random.choice([True, False]):
                print("Congratulations! You found the treasure!\n")
                break  # Exit the loop if the player finds the treasure
            else:
                print("The chest is trapped! You get caught!\n")
        elif action == 'leave':
            print("You wisely left the cave and returned to the forest.\n")
        else:
            print("Invalid choice! You panic and run back!\n")

    # If the player chooses the River
    elif choice == '2':
        print("\nYou approach the River.")
        action = input("You see a fishing boat. Do you want to 'row' or 'swim'? ")
        if action == 'row':
            print("You row to the other side and find a hidden path to the treasure! You escape with treasure!\n")
            break  # Exit the loop if the player finds the treasure
        elif action == 'swim':
            # Random chance to find treasure or get swept away
            if random.choice([True, False]):
                print("You swam across safely and found the treasure!\n")
                break  # Exit the loop if the player finds the treasure
            else:
                print("You got swept away by the current! Be careful next time!\n")
        else:
            print("Invalid choice! You slip and fall into the water!\n")

    # If the player chooses the Old Tree
    elif choice == '3':
        print("\nYou approach the Old Tree.")
        action = input("There's a key under the tree. Do you want to 'take' it or 'ignore' it? ")
        if action == 'take':
            print("You took the key! It unlocks a secret treasure nearby!\n")
            break  # Exit the loop if the player finds the treasure
        elif action == 'ignore':
            print("You walked away and missed the treasure!\n")
        else:
            print("Invalid choice! You get lost in thought!\n")

    # If the player makes an invalid choice
    else:
        print("Invalid choice! Please choose 1, 2, or 3.\n")

# End of the game
print("Thanks for playing! Hope you enjoyed the adventure.")
