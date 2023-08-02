'''Given an array A[1 .. n] of integers, compute the length of a longest alternating subsequence. A sequence B[1 .. l] is alternating if B[i] < B[i − 1] for every even index i ≥ 2, and B[i] > B[i − 1] for every odd index i ≥ 3. For example, given the array
⟨3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 7⟩
your algorithm should return the integer 17, because 3, 1, 4, 1, 5, 2, 6, 5, 8, 7, 9, 3, 8, 4, 6, 2, 7 is a longest alternating subsequence (one of many).
'''

def LAS(arr, n):
    inc = 1
    dec = 1
    for i in range(1, n):
        if (arr[i] > arr[i-1]):
            inc = dec + 1
        elif (arr[i] < arr[i-1]):
            dec = inc + 1
    return max(inc, dec)
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 7]
    n = len(arr)
    print(f'The Longest Alternating Subsequence is {LAS(arr, n)}')

