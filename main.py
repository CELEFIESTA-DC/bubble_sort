#!/usr/bin/python3

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            if array[i] <= array[j+1]:
                array[i], array[i+1] = array[i], array[i+1] 
    return array
