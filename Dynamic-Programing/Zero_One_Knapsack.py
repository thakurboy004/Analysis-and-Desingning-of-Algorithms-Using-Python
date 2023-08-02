'''Implement 0/1 Knapsack problem using dynamic programming.
'''

def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items[::-1]

if __name__ == '__main__':
    weights = [3, 2, 4, 1]
    values = [5, 3, 8, 2]
    capacity = 6
    max_value, selected_items = knapsack(weights, values, capacity)
    print(f"Maximum value: {max_value}")
    print(f"Selected items: {selected_items}")
