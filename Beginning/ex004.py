formatter = "{} lol {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One", "Two", "Three", "Four", "Five"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Here comes",
    "My lastest haiku",
    "It is so damn good",
    "You'll cry when you hear it"
))
