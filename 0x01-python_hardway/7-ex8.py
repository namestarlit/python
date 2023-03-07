formatter = "{} {} {} {} "

# using a format function to pass arguments
# to the formatter strings, by replacing
# the {} with a respective value in .format() function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "This is something",
    "else indeed.",
    "Let's see this",
    "Art of python."
    ))
