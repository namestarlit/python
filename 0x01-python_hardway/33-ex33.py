# initialize i to 0
i = 0
size = 6
numbers = []

# while-loop to append values into numbers list
while i < size:
    print(f"At the top i is {i}")
    numbers.append(i)

    # update i, increment by 1
    i = i + 1
    print("Numebrs now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

# for loop to print numbers
for num in numbers:
    print(num)
