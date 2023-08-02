'''Implement MCM algorithm for the given n matrix <M1xM2...............Mn> where the size of the matrix is Mi=di-1 x di.
'''

def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

if __name__ == '__main__':
    dimensions = [10, 30, 5, 60]
    minimum_scalar_multiplications = matrix_chain_multiplication(dimensions)
    print(f"Minimum number of scalar multiplications: {minimum_scalar_multiplications}")
