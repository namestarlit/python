from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying file from {from_file} to {to_file}.")

# we could do these two on one line, how?
in_file = open(from_file) # open source file in read mode
indata = in_file.read() # read and store data into indata variable

# check lenght of the file in bytes
print(f"The input file is {len(indata)} bytes long")

# check if the destination file exists
# using exists() function
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# open destination file
out_file = open(to_file, 'w')
# write the data from source file into it
out_file.write(indata)

print("Alright, all done")

# close the files
out_file.close()
in_file.close()
