#!/usr/bin/python3

"""
thx @ https://github.com/Maschamagin for the indication 
"""

def readFile(filePath):
    """Read the content of a passed file as string and strip each line

    Return filecontent as list
    """
    
    with open(filePath) as fileContent:
        content = fileContent.readlines()
        content = [c.strip() for c in content]
        return content

def getLineNumber(areaLines):
    """Get the number of lines and the length of each line

    Because all lines have equal length, check length of line for 1. Line
    print 
    The Values are just for the input inspection and not necessary 
    to solve the challenge 
    """

    lineNumber = len(areaLines)
    lineLength = len(areaLines[0])
    return lineNumber, lineLength

def getTreeNumber(areaLines, treeCounter):
    """Go through each line and check if position is a tree

    each line is one step down
    counter + 3 is three steps right
    if counter is equal or greater 31 set counter -31 to get all three cases
    """
    counter = 0
    for line in areaLines:
        print(line)
        print(counter)
        if (line[counter] == '#'):
            treeCounter +=1
        counter += 3
        if (counter >= 31):
            counter -= 31
        
    return treeCounter

def main():
    filePath = ('input.txt')
    treeCounter = 0
    areaLines = readFile(filePath)
    lineNumber, lineLength = getLineNumber(areaLines)
    treeCounter = getTreeNumber(areaLines, treeCounter)
    print(lineNumber)
    print(lineLength)
    print(treeCounter)

if __name__ == '__main__':
    main()