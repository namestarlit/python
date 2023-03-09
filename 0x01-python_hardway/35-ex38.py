ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fic that.")

# splits the string using spaces as delimeter
stuff = ten_things.split(' ')
more_stuff = ["Days", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

# adds elements until lenght of stuff is 10
while len(stuff) != 10:
    # pops the last element from more_stuff
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # appends the popped element into stuff
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

# prints the element at index 1
print(stuff[1])
# prints the last element
print(stuff[-1])
# print the last element
print(stuff.pop())
# joins elements with a space in between
print(' '.join(stuff))
# joins elements from index 3 to 4 with a # in between
print('#'.join(stuff[3:5]))
