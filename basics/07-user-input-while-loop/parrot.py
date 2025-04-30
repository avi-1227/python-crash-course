# How th input() Function Works
# The input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Sometimes you'll want to write a prompt that's longer than one line.

prompt = "If you tell us who you are, we can personalize the message you see."
prompt+= "\nwhat is your first name?: "

name = input(prompt)
print(f"Hello, {name}!")

# Using int() to Accept Numerical Input
'''When you use the input() function, Python interprets everything the user enters as a string.'''

height = input("How tall are you, in inches?: ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.") 