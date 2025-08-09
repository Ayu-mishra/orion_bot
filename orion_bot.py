import random

import datetime


# Predefined responses
jokes = [
    "What's a programmer's favorite place? – The Loop.",
    "Why did the Python programmer go to the beach? – Because he didn't know C.",
    "What's a programmer's favorite drink? – Java."
]


quotes = [
    "A coder’s prayer: May your code be bug-free and run smoothly. ",
    "Every error has a solution; it just requires a little patience to install.",
    "Even the best-written code can fail, but the joy of debugging is unmatched."
]


greetings = ["Hi", "Hello", "Hey", "Greetings"]


# Memory for user's name
user_name = None


def orion_response(user_input):
    global user_name
    user_input_lower = user_input.lower()


# Greeting
    if any(greet.lower() in user_input_lower for greet in greetings):
        if user_name:
            return f"{random.choice(greetings)}, {user_name}! How are you today?"
        else:
            return f"{random.choice(greetings)}! What's your name?"


# Name capture
    elif "my name is" in user_input_lower:
        user_name = user_input.split()[-1].capitalize()
        return f"Nice to meet you, {user_name}!"


# Time
    elif "time" in user_input_lower:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."


# Date
    elif "date" in user_input_lower:
        return f"Today's date is {datetime.date.today()}."


# Joke
    elif "joke" in user_input_lower:
        return random.choice(jokes)


# Quote/motivational line
    elif "quote" in user_input_lower or "motivate" in user_input_lower:
        return random.choice(quotes)


# Exit
    elif "bye" in user_input_lower:
        return f"Goodbye {user_name if user_name else ''}, see you next time!"


# Default fallback
    else:
        return "I’m not sure I understand, but I’m listening."

# Run Orion
print("Professional Python Assistant: Orion | Type 'bye' to exit\n")


while True:
    user_input = input("You: ")
    response = orion_response(user_input)
    print("Orion:", response)
    if "bye" in user_input.lower():
        break
