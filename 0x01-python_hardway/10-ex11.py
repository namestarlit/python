# end=' ' connects the next print statement
# with the preceeding one.
print("How old are you?", end=' ')
age = input()

# input() function reads input from user
# or standard input (stdin)
print("How tall are you?", end=' ')
height = input()

print("How much do you weigh?", end=' ')
weight = input()

# printing all the input data using the f.string functionality
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
