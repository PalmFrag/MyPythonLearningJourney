from sys import argv

scriptname, filename = argv

print(f"I'm about to erase {filename}.")
print("To avert this, hit CTRL-C(^C)")
print(f"If you wish for {filename}'s dead, hit RETURN'")

input("Your order? > ")

print("Opening the file...")
target = open(filename, 'w')
print(f"Sayonara, {filename}-san... Truncated!")
target.truncate()

print(f"Now let's give {filename}-san a new meaning, write something in it please:")
print("Only 3 lines though")
line1 = input("First line: ")
line2 = input("Second line: ")
line3 = input("Third line: ")

print(f"Giving {filename}-kun its new identity...")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("Saving...")
target.close()
print(f"Done, {filename}-kun has been reborn and its new identity reads as follows:")

new_file = open(filename)

print(new_file.read())
print(f"Hope you like killing {filename}-san to give birth to this beast!")
