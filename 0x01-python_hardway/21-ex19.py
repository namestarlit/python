# declare a function cheese_and_crackers that takes
# two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes fo crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# call a function directly
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# assign the values to variables and pass in
# variables as arguments
print("OR, we can use variables from out script:")
amount_of_cheese = 10
amount_of_crackers = 50

# calling and passing arguments to the function parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# passing arithmetic of values as arguments
print("we can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# combining variables and numbers as arguments to the function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
