'''Implement OBST for given n keys (K1,K2.....Km) whose pi and qi (dummy keys) are given.
'''

class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

def construct_obst(keys, p, q):
    n = len(keys)


    cost = [[0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * n for _ in range(n)]

    
    for i in range(1, n + 2):
        cost[i][i - 1] = q[i - 1]

    
    def calculate_cost(i, j):
        if i <= j:
            if cost[i][j] != 0:
                return cost[i][j]

            min_cost = float('inf')

     
            for r in range(i, j + 1):
                c = calculate_cost(i, r - 1) + calculate_cost(r + 1, j) + sum(p[i - 1:j]) + sum(q[i - 1:j + 1])
                if c < min_cost:
                    min_cost = c
                    root[i - 1][j - 1] = r

            cost[i][j] = min_cost

        return cost[i][j]

    calculate_cost(1, n)

    def build_obst(i, j, parent):
        if i <= j:
            r = root[i - 1][j - 1]
            node = Node(keys[r - 1], parent)
            node.left = build_obst(i, r - 1, node)
            node.right = build_obst(r + 1, j, node)
            return node
        else:
            return None

    
    root_node = build_obst(1, n, None)

    return root_node

def print_obst(root, level=0):
    if root:
        print("  " * level, root.key)
        print_obst(root.left, level + 1)
        print_obst(root.right, level + 1)


keys = [10, 12, 20, 25]
p = [0.1, 0.2, 0.3, 0.4]
q = [0.05, 0.1, 0.05, 0.1, 0.2]

root = construct_obst(keys, p, q)
print('OBST')
print_obst(root)
