#
# start.py
#

def stripNewlines(line):
    strippedLine = "";

    for character in line:
        if character != "\n":
            strippedLine += character


    return strippedLine

def main():
    inputFile = open("test.js", "r+")
    for line in inputFile:
        print stripNewlines(line)

main()
