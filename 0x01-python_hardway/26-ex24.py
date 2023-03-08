# working with strings and escape sequences
print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do:')
print('\n newlines and \t tabs.')

# multiline strings
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# printing the sorrowful poem
print("--------------------")
print(poem)
print("--------------------")


# assigning value and some math
five = 10 - 2 + 3 - 6
# printing using format string (f.string)
print(f"This should be five: {five}")

# defining functions
def secret_formula(started):
    # we can actully do some maths in it
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # return three values
    return jelly_beans, jars, crates


# store the start value into a variable
start_point = 10000
# pass variable to the function
# and store the return values into variables respectively from left
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# reduce the start value
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
