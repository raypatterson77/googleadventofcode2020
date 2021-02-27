#!/usr/bin/python3

"""
thx @ https://github.com/Maschamagin for the indication
"""

def read_file(file_path):
    """Read the content of a passed file as string and strip each line

    Return filecontent as list
    """

    with open(file_path) as file_content:
        content = file_content.readlines()
        content = [c.strip() for c in content]
        return content

def get_line_number(area_lines):
    """Get the number of lines and the length of each line

    Because all lines have equal length, check length of line for 1. Line
    print
    The Values are just for the input inspection and not necessary
    to solve the challenge
    """

    line_number = len(area_lines)
    line_length = len(area_lines[0])
    return line_number, line_length

def get_tree_number(area_lines, tree_counter):
    """Go through each line and check if position is a tree

    each line is one step down
    counter + 3 is three steps right
    if counter is equal or greater 31 set counter -31 to get all three cases
    """
    counter = 0
    for line in area_lines:
        if line[counter] == '#':
            tree_counter +=1
        counter += 3
        if counter >= 31:
            counter -= 31
    return tree_counter

def main():
    file_path = ('input.txt')
    tree_counter = 0
    area_lines = read_file(file_path)
    line_number, line_length = get_line_number(area_lines)
    tree_counter = get_tree_number(area_lines, tree_counter)
    print(line_number)
    print(line_length)
    print(tree_counter)

if __name__ == '__main__':
    main()
    