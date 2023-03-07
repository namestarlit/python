types_of_people = 10
# f.string (format string), assigns the value of variable
# in the place of {avariable}
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# f.string inserts the value of x and y
# at the place holders{x} and {y} respectively
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assign values to variables
hilarious = False
joke_evaluation = "Isn't that joke so funnny?! {}"

# .format() inserts the value of hilarious
# into the space '{}' in the joke_evaluation string
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

# prints the values of w and e respectively
print(w + e)
