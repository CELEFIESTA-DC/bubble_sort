#!/usr/bin/python3
"""
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted.

eg:
    >>> bubble_sort([10,2,3,4,1])
    [1,2,3,4,10]
"""
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            if array[i] <= array[j+1]:
                array[i], array[i+1] = array[i], array[i+1] 
    return array
