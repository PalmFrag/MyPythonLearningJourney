from sys import argv

script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you love me {user_name}? ")
likes = input(prompt)

print(f"Where do you live {user_name}? ")
lives = input(prompt)

print("What kind of computer do you have? ")
computer = input(prompt)

print(f"""
Ok, you said {likes} about liking me.
You supposedly live in {lives}. Dunno where it is though.
And you have a {computer}, that's a garbage pc.
""")
