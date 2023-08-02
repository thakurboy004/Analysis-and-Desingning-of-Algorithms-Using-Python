'''Write a program to Implement breadth first search algorithm for given graph G.
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
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node) 
    while queue:
        m=queue.pop(0)
        print(m,end=' \n')
        for neighbr in graph [m]:
            if neighbr not in visited:
                queue.append(neighbr)
                visited.append(neighbr)               
print('BFS')
bfs(visited,graph,'0,0')
