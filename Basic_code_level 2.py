# Weather-Based Activity Suggestion.

# Asking user to enter the current weather condition
weather = input("What is the weather like today (sunny, rainy, cloudy, snowy)? ").lower()

# Using if-elif-else to suggest activites based on weather conditions.
if weather == "sunny":
    print("It's a beautiful day! How about going for a hike or having a picnic?")
elif weather == "rainy":
    print("Looks like it's raining. Maybe you could cozy up with a book or watch a movie indoors.")
elif weather == "cloudy":
    print("A bit cloudy today. A nice walk or visting a museum might be a good idea.")
elif weather == "snowing":
    print("Its's snowy outside! Time for buliding a snowman or enjoying some hot chocolate by the fire.")
else:
    print("Hmm, I'm not sure about that weather conditinon. Please enter sunny, rainy, cloudy, or snowy.")