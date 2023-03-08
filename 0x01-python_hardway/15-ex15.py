from sys import argv

script, filename = argv

# open() function opens a file
# opens in read text mode ("rt") by default
# if no mode arguments are provided
txt = open(filename)

print(f"Here's your file {filename}")
# print() prints the content of filename
# read() function reads a file
print(txt.read())

# close the file using close() function
txt.close()

print("Type the filename again")
# read file name from stdin/user using input()
file_again = input("> ")
# open the file using open()
txt_again = open(file_again)

# print content of the file
# using print() and read() functions
print(txt_again.read())

# close the file using close() function
txt_again.close()
