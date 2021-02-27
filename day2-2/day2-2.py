#! /usr/bin/python3

import re

def readFile(filePath):
    """Read the content of a passed file as string and strip each line

    Return filecontent as list
    """
    
    with open(filePath) as fileContent:
        content = fileContent.readlines()
        content = [c.strip() for c in content]
        return content

def getParameters(passwordLine):
    """Get all Parameters: pos1, pos2, char, password

    Split by - : Whitepsace
    Remove Whitespace From List
    ToDo: Python Regex research why the second whitespace is added to list 
    """

    parameterList = re.split('[-:\s+]', passwordLine)
    parameterList.remove('')
    return parameterList

def interatePasswords(passwordPolicies, validPwCounter):
    """Go Through the list of passwords and check the policy

    Get validCounter from main()
    Get the parameters of the policy and the password with getParameters() as list

    go through each char of the password and check if Position 1 & 2
    match policy
   
    Returns the number of valid passwords 
    """
    
    for passwordLine in passwordPolicies:
        parameterList = getParameters(passwordLine)
        pos1 = int(parameterList[0])-1
        pos2 = int(parameterList[1])-1
        policyChar = parameterList[2]
        password = parameterList[3]
        if (bool(password[pos1] == policyChar) != bool(password[pos2] == policyChar)):
            validPwCounter = validPwCounter + 1
    return validPwCounter


def main():
    filePath = ('input.txt')
    validPwCounter = 0
    passwordPolicies = readFile(filePath)
    countedValidPasswords = interatePasswords(passwordPolicies, validPwCounter)
    print(countedValidPasswords)

if __name__ == '__main__':
    main()