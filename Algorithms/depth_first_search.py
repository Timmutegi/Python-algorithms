"""
The illustrated graph is represented using an adjacency list
An easy way to do this in Python is to use a dictionary data structure,
where each vertex has a stored list of its adjacent nodes

Since all the nodes and vertices are visited, the time complexity for DFS on a
graph is O(V + E); where V is the number of vertices and E is the number of edges.

In case of DFS on a tree, the time complexity is O(V), where V is the number of nodes.
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set that is used to keep track of visited nodes
visited = set() 

"""
1. First checks if the current node is unvisited - if yes, it is appended in the visited set.
2. Then for each neighbour of teh current node, the dfs function is invoked again.
3. The base case is invoked when all the nodes are visited. The function then returns.
"""
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')