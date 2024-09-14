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

# Age-Based Activity Recommendation

# Ask user to enter their age
age = int(input("Please enter your age: "))

#Using if-elif-else to recommend activities based on age groups.
if age <12:
    (print("You are quite young! How about visiting the zoo or playing some fun video games?"))
elif 12 <= age < 18:
    print("You might enjoy some outdoor sports like soccer or basketbll, or maybe going to an amusement park.")
elif 18 <= age < 30:
    print("How about trying some new hobbies like hiking, traveling or learing new skills?")
elif 30 <= age <60:
    print("Maybe you'd enjoy a mix of leisure activites, like cooking, yoga,or even a weekend getaway.")
elif age >=60:
    print("It's the perfect time to relax and enjoy things like gardening, reading, or spending time wqith loved ones.")
else:
    print("That's an intersting age! Feel free to do anything that makes you happy.")