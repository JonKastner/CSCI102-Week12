# Jonathon Kastner
# CSCI 102 - Section C
# Week 12 - Part B

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(filename):
    f = open(filename)
    lines = []
    for line in f:
        lines.append(str.strip(line))
    f.close()
    return lines

def UpdateString(string1, string2, index):
    my_list = list(string1)
    my_list[index] = string2
    new_string = "".join(my_list)
    print('OUTPUT',new_string)


UpdateString("Hello World", "a", 3)
