class JavascriptLinter:
    version = "1.0"
    inputFile = None
    filePointer = None
    lines = [ ]

    def __init__(self, inputFile):
        print "JavascriptLinter v" + self.version
        print "File to lint: \"" + inputFile + "\""
        self.inputFile = inputFile
        self.filePointer = open(self.inputFile, "r+")
        self.lines = self.getLines()


    def stripNewlines(self, line):
        retLine = ""
        for character in line:
            if character != "\n":
                retLine += character
        return retLine

    def getLines(self):
        lines = []
        for line in self.filePointer:
            lines.append(self.stripNewlines(line))

        return lines

    def lint(self, line):
        if str(line).find("console") != -1:
            print "I saw console!"

    def lintFile(self):
        for line in self.lines:
            self.lint(line)

JavascriptLinter("test.js");
