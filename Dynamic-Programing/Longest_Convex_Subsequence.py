'''Given an array A[1 .. n] of integers, compute the length of a longest convex subsequence of A. A sequence B[1 .. l] is convex if B[i] − B[i − 1] > B[i − 1] − B[i − 2] for every index i ≥ 3.
'''

def longest_convex_subsequence(arr):
    n = len(arr)
    if n <= 2:
        return n

    longest_subseq_length = [2] * n

    for i in range(2, n):
        for j in range(i-1, 0, -1):
            if arr[i] - arr[j] > arr[j] - arr[j-1]:
                longest_subseq_length[i] = max(longest_subseq_length[i], longest_subseq_length[j] + 1)

    return max(longest_subseq_length)

if __name__ == '__main__':
    A = [1, 2, 4, 3, 7, 6, 5, 9, 8]
    length = longest_convex_subsequence(A)
    print(f"Length of the longest convex subsequence: {length}")
