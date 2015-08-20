
class JavascriptLinter:
    version = "1.0"
    inputFile = None
    filePointer = None
    lines = [ ]
    errors = [ ]
    warnings = [ ]
    style = [ ]

    def __init__(self, inputFile):
        print ("JavascriptLinter version " + self.version)
        print ("File to lint: \"" + inputFile + "\"")
        self.inputFile = inputFile
        self.filePointer = open(self.inputFile, "r+")
        self.lines = self.getLines()

    def getLines(self):
        lines = []
        for line in self.filePointer:
            lines.append(line.replace("\n", ""))

        print ("There are " + str(len(lines)) + " lines in " + str(self.inputFile))

        return lines

    def lintLine(self, line):
        if str(line).find("console") != -1:
            print ("I saw console!")

    def lintFile(self):
        for line in self.lines:
            self.lintLine(line)

JavascriptLinter("test.js")