from sys import argv

script, input_file = argv

# a function that reads a file
# and prints its content
def print_all(f):
    print(f.read())

# a function that sets the cursor at
# initial position of cursor
def rewind(f):
    f.seek(0)

# a function to print a line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind , kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# set current_line to 1
current_line = 1
print_a_line(current_line, current_file)

# increment the line count by 1
current_line += 1
print_a_line(current_line, current_file)
# increment line count by 1 more line
current_line += 1
print_a_line(current_line, current_file)
