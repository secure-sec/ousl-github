
# input  user  name
name = input("What's your name? ").strip()  

# Check if the user entered a name
if not name:
    print("You didn't enter a name. I'll just call you 'Guest'.")
    name = "Guest"

 # user  feeling check 
feeling = input(f"Hi {name}! How are you feeling today? ").strip()

# Provide a response based on their input
if feeling.lower() in ["good", "great", "fine", "happy"]:
    print(f"That's wonderful to hear, {name}! Keep up the positive vibes! 😊")
elif feeling.lower() in ["bad", "not good", "sad", "tired"]:
    print(f"I'm sorry to hear that, {name}. I hope things get better soon! 🌟")
else:
    print(f"Thanks for sharing, {name}. Let's have a great day together! 🚀")

# output
print("Have fun exploring Python programming!")
