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

lines = LoadFile('test.txt')
print('OUTPUT',lines)
