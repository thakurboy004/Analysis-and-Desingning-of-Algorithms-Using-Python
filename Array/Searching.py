'''Revise pseudocode for searching within an array (int, float, or char type) using
following searching techniques:
● Linear Search
● Binary Search
A. Plot the complexity chart for n=10 to 100.
B. Analyse their complexities in best case, average case and worst case.
'''

import matplotlib.pyplot as plt
import time
import random
    
def linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
                return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def binary(arr, x):
    binarySearch(arr, 0, len(arr)-1, x)
    
def plot(search, title):
    x = [x for x in range(1,10000,1000)]
    y = []
    for i in x:
        start = time.perf_counter()
        search(random.sample(range(10000), i), random.randrange(1000))
        end = time.perf_counter()
        y.append(end-start)
    
    plt.plot(x, y)
    plt.xlabel("N")
    plt.ylabel("Time")
    plt.title(title)

plot(linear, "Linear Search")
plot(binary, "Binary Search")
plt.title("Searching Time complexity")
plt.show()

