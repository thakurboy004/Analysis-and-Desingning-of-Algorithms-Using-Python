'''Given an array A[1 .. n], compute the length of a longest palindrome subsequence of A. Recall that a sequence B[1 .. l] is a palindrome if B[i] = B[l− i + 1] for every index i.
'''

def Seq(A , B, m, n):
    dp = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[m][n]
def LPS(A, n):
    b = ""
    for i in A:
        b = i + b
    print('The reversed string of the following will be ', b)
    val = Seq(A, b, n, len(b))
    return val
if __name__ == '__main__':
    a = "AFTERAGOODCUPOFTEA"
    n = len(a)
    print(f'The Longest Palindrome Sebsequence of the following is {LPS(a, n)}')
