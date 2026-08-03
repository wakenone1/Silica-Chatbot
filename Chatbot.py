# So I have to build a chatbot according to a designated framework
from datetime import datetime
import time
import random as rand
class Robot:
    def __init__(self, name, model, model_completeness):
        self.name = name
        self.model = model
        self.model_completeness = model_completeness

robot = Robot("Silica", "Version 0.0.0.1", "Incomplete" )
print(f"Chatbot name : {robot.name}, {robot.model}, Model status: {robot.model_completeness}")
print("Hello, I am Silica. Your Pybot companion.")

# Effect Functions:
def typindicator():
    print("Typing", end="", flush=True)
    for i in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\b\b\b\b\b\b\b\b\b \b\b\b\b\b\b\b\b\b", end="")

user = {"sad": "You don't have to go through this alone, find someone who can help you in real life.", "tired": "Take some rest then.", "happy": "Oh, enjoy!", "angry": "Calm down, tiger! XD", "bored": "Go do something fun!", "help": """For time : Type 'time'
For quitting : Type 'quit'"""}
user_input = ""
while True:
    user_input = input("User : ")
    

    if "hi" in user_input.lower() or "hello" in user_input.lower() or "hey" in user_input.lower():
        greet_dict = ["Hey, nice to have you here! How are you feeling today?", "Hi, it's great to have you here! What's the mood?", "Hello user! How are you today?"]
        bot_choice = rand.choice(greet_dict)
        typindicator()
        print(bot_choice)
    elif "sad" in user_input.lower() or "depressed" in user_input.lower():
        typindicator()
        print(user["sad"])
    elif "angry" in user_input.lower() or "mad" in user_input.lower():
        typindicator()
        print(user["angry"])
    elif "happy" in user_input.lower() or "well" in user_input.lower() or "fine" in user_input.lower():
        typindicator()
        print(user["happy"])
    elif "bored" in user_input.lower():
        typindicator()
        print(user["bored"])
    elif "tired" in user_input.lower() or "exhausted" in user_input.lower():
        typindicator()
        print(user["tired"])
    elif user_input.lower() == "help":
        print()
        print(user["help"])
        print()
    elif "quit" in user_input.lower():
        typindicator()
        print("It was nice talking to you. Have a great day!")
        break
    elif "time" in user_input.lower():
        now = datetime.now()
        typindicator()
        print(now)
    else:
        error_handling = ["Sorry, I don't understand the input, please try again.", "Failed to process, please try again.", "Invalid input, please try again."]
        choice = rand.choice(error_handling)
        typindicator()
        print(choice)
    


