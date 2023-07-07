'''Here graph is dictionary with keys and values'''
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[],
}
#BFS-we use Queue
visited=[]#List for visited nodes
queue=[]#initialize the queue
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:#creating loop to visit each node
        m=queue.pop(0)
        print(m,end=' ')
        for i in graph[m]:
            visited.append(i)
            queue.append(i)
bfs(visited,graph,'3')
