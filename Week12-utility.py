# Jonathon Kastner
# CSCI 102 - Section C
# Week 12 - Part A/B

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

def FindWordCount(the_list, string):
    count = 0
    for line in the_list:
        count += line.count(string)
    return count

def ScoreFinder(names, scores, target):
    target = target.capitalize()
    if target in names:
        index = names.index(target)
        print('OUTPUT', target, 'got a score of', scores[index])
    else:
        print('OUTPUT player not found')

def Union(list1, list2):
    new_list = []
    for element in list1:
        if element not in new_list:
            new_list.append(element)
    for element in list2:
        if element not in new_list:
            new_list.append(element)
    return new_list

def Intersection(list1, list2):
    new_list = []
    for element in list1:
        if element in list2:
            new_list.append(element)
    return new_list

def NotIn(list1, list2):
    new_list = []
    for element in list1:
        if element not in list2:
            new_list.append(element)
    return new_list
