from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")

input("? ")

print("Opening the file...")
# open file in write mode 'w'
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# truncate() function truncates the file
target.truncate()

print("Now, I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm goint to write these to the file.")

# write() function writes into the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
