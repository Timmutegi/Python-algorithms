"""
The illustrated graph is represented using an adjacency list
An easy way to do this in Python is to use a dictionary data structure,
where each vertex has a stored list of its adjacent nodes

Since all the nodes and vertices are visited, the time complexity for BFS on a
graph is O(V + E); where V is the number of vertices and E is the number of edges.
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# List that is used to keep track of visited nodes
visited = [] 

# List used to keep track of nodes currently in the queue
queue = []

"""
1. Checks and appends the starting node to the visited list and the queue
2. Then, while the queue contains elements, it keeps taking out nodes from the queue,
    appends the neighbours of that node to the queue if they are unvisited, and markes them as visited.
3. This continues until the queue is empty
"""
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        poppedNode = queue.pop(0)
        print(poppedNode, end = " ")

        for neighbour in graph[poppedNode]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver code
bfs(visited, graph, 'A')