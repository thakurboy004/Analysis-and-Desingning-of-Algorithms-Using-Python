'''Revise pseudocode for sorting an array (int, float, or char type) using following
sorting techniques:
● Selection sort
● Bubble sort
● Merge sort (Recursive)
● Quick sort (Recursive)
A. Plot the complexity chart for n=10 to 100.
B. Analyse their complexities in best case, average case and worst case.
'''

import matplotlib.pyplot as plt
import time
import random

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0  
    j = 0   
    k = l    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge_sort(arr, l, m, r)

def merge(arr):
    mergeSort(arr, 0, len(arr)-1)
    
# Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def quick(arr):
    quickSort(arr, 0, len(arr)-1)
    
def plot(sort, title):
    x = [x for x in range(10,1000,5)]
    y = []
    for i in x:
        start = time.perf_counter()
        sort(random.sample(range(1000), i))
        end = time.perf_counter()
        y.append(end-start)
    plt.plot(x, y, label = title)
    plt.title(title)

plot(selection_sort, "Selection Sort")
plot(bubble_sort, "Bubble Sort")
plot(merge, "Merge Sort")
plot(quick, "Quick Sort")

plt.title("Sorting Time Complexity")    
plt.xlabel("N")
plt.ylabel("Time")
plt.legend()
plt.show()
