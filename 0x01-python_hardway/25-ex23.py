import sys
script, encoding, error = sys.argv


# defining a main function
def main(language_file, encoding, errors):
    # read a single line from the languages.txt file
    line = language_file.readline()
    
    # use an if statement to execute only
    # when there's a line
    if line:
        # calling print_line function to print the line
        print_line(line, encoding,errors)
        # calling main inside main, makes main
        # a recursive function (it loops)
        # if statement prevents it from looping forever
        return main(language_file, encoding, errors)


# defining print_line function
def print_line(line, encoding, errors):
    # strip the newline character at the end of each line
    next_lang = line.strip()
    # encode strings from the file
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # decode raw bytes into strings
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<==>", cooked_string)


# open the languages.txt file
languages = open("24-languages.txt", encoding="utf-8")

# call the main function, it will loop
main(languages, encoding, error)
