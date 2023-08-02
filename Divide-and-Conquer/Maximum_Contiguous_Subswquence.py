'''Maximum Value Contiguous Subsequence: Given a sequence of n numbers A(1) ...A(n),give an algorithm for finding a contiguous subsequence A(i) ...A(j) for which the sum of elements in the subsequence is maximum. Example : {-2, 11, -4, 13, -5, 2} → 20 and {1, -3, 4, -2, -1, 6 } → 7.'''

maxint = 7
def maxSubArraySum(a, size):
    curmax= -maxint - 1
    finalmax = 0
    for i in range(0, size):
        finalmax = finalmax + a[i]
        if (curmax < finalmax):
            curmax = finalmax

        if finalmax < 0:
            finalmax = 0
    return curmax
if __name__ == '__main__':
    a = [-67, -3, 89, -1, -2, 1, 5, -3]
    print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))

