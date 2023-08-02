'''' Let there be an array of N random elements. We need to sort this array in ascending order. If n is very large (i.e. N= 1,00,000) then Quicksort may be considered as the fastest algorithm to sort this array. However, we can further optimize its performance by hybridizing it with insertion sort. Therefore, if n is small (i.e. N<= 10) then we apply insertion sort to the array otherwise Quick Sort is applied. Implement the above discussed hybridized Quick Sort and compare the running time of normal Quick sort and hybridized quick sort. Run each type of sorting 10 times on a random set of inputs and compare the average time returned by these algorithms'''

import matplotlib.pyplot as plt
import time
import random
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j>low and arr[j-1]>val:
            arr[j]= arr[j-1]
            j-= 1
        arr[j]= val
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
    
def hybrid_quick_sort(arr, low, high):
    while low<high:

        if high-low + 1<10:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)

            if pivot-low<high-pivot:
                hybrid_quick_sort(arr, low, pivot-1)
                low = pivot + 1
            else:

                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot-1
def hybrid(arr):
    hybrid_quick_sort(arr, 0, len(arr)-1)
    
def plot(sort, title):
    x = [x for x in range(10,1000,10)]
    y = []
    for i in x:
        start = time.perf_counter()
        sort(random.sample(range(1000), i))
        end = time.perf_counter()
        y.append(end-start)
    plt.plot(x, y, label = title)
    plt.title(title)

plot(quick, "Quick Sort")
plot(hybrid, "Hybrid sort")

plt.title("Time Complexity Comparison")    
plt.xlabel("N")
plt.ylabel("Time")
plt.legend()
plt.show()
