''' Write a program to find the strongly connected components in a Graph.
'''

from collections import defaultdict


def kosaraju(graph):
    stack = []
    visited = [False] * len(graph)
    components = []
    numComponents = 0

    def dfs_1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_1(neighbor)
        stack.append(node)

    def dfs_2(node):
        print(node)
        component[node] = numComponents
        components[numComponents].append(node)
        visited[node] = True
        for neighbor in graph_rev[node]:
            if not visited[neighbor]:
                dfs_2(neighbor)

    for node in range(len(graph)):
        if not visited[node]:
            dfs_1(node)

    visited = [False] * len(graph)
    component = [None] * len(graph)

    while stack:
        node = stack.pop()
        if not visited[node]:
            print("Component " + str(numComponents) + ":")
            components.append([])
            dfs_2(node)
            numComponents += 1

    return components


graph = defaultdict(list)
graph[0] = [1]
graph[1] = [2]
graph[2] = [0, 3]
graph[3] = [4]
graph[4] = [5]
graph[5] = [3, 6]
graph[6] = [7]
graph[7] = [6]

graph_rev = defaultdict(list)
graph_rev[1] = [0]
graph_rev[2] = [1]
graph_rev[0] = [2]
graph_rev[3] = [2, 5]
graph_rev[4] = [3]
graph_rev[5] = [4]
graph_rev[6] = [5, 7]
graph_rev[7] = [6]

strongly_connected_components = kosaraju(graph)
print("Strongly Connected Components:")
for component in strongly_connected_components:
    print(component)
3