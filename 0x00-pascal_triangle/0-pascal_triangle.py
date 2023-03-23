#!/usr/bin/python3

''' code prints pascal's triangle '''


def pascal_triangle(n):
    my_list = []
    if (n <= 0):
        return my_list
    my_list.append([1])
    for i in range(n - 1):
        my_list.append([i]+[my_list[i][a]+my_list[i][a + 1]
                            for a in range(len(my_list[i]) - 1)] + [1])
    return my_list
