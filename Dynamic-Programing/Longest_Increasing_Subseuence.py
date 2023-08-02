''' Given an array A[1 .. n] of integers, compute the length of a longest increasing subsequence. A sequence B[1 .. l] is increasing if B[i] > B[i − 1] for every index i ≥ 2. For example, given the array
 ⟨3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 7⟩
your algorithm should return the integer 6, because 1, 4, 5, 6, 8, 9 is a longest increasing subsequence (one of many).
'''

def LIS(arr, n):
    a = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if(arr[j]<arr[i]):
                a[i] = max(a[i], a[j]+1)
    return max(a)
if __name__ == '__main__':
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 7]
    length = LIS(arr, len(arr))
    print(f"The Longest Increasing Subsequence is {length}")

