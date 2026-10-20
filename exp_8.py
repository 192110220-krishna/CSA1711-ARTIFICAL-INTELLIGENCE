
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor, visited)

start = input("Enter starting node (A-F): ").upper()

if start in graph:
    print("DFS Traversal:")
    dfs(start, set())
else:
    print("Invalid starting node!")
    
print()
