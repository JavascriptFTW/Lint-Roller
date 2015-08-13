#
# start.py
#

def main():
    inputFile = open("test.js", "r+")
    for line in inputFile:
        lnToPrint = ""
        for character in line:
            # Make sure this isn't a silly newline, if it isn't, we can print this character.
            if character != "\n":
                lnToPrint += character

        print lnToPrint

main()
