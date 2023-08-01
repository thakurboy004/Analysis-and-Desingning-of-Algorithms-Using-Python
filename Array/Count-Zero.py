'''You have been given a sorted array ARR (of size M, where M is very large) of two
elements, 0 and 1. It is desired to compute the count of 0s in the array ARR. Propose and
implement an efficient algorithm to accomplish the task.'''

def count_zero(arr):
    x = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid+1

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1
if __name__ == '__main__':
 
    arr = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
 
    print("Count of 0's in given array is ", count_zero(arr))


