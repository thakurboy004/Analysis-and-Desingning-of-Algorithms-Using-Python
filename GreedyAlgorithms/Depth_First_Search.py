'''Write a program to Implement depth first search algorithm for given graph G.
'''

graph={'0,0':['5,0','0,3'],
       '5,0':['5,3','2,3'],
       '5,3':[],
       '2,3':['2,0'],
       '2,0':['0,2'],
       '0,2':['5,2'],
       '5,2':['4,3'],
       '4,3':['4,0'],
       '0,3':['3,0'],
       '3,0':['3,3'],
       '3,3':['5,1'],
       '5,1':['0,1'],
       '0,1':['1,0'],
       '1,0':['1,3'],
       '1,3':['4,0'],
       '4,0':[]
      }    
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node, end="->")
        visited.add(node)
        for neighbr in graph[node]:
            dfs(visited,graph,neighbr)
print('DFS')
dfs(visited,graph,'0,0')
