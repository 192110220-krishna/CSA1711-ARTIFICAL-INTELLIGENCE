
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0
}

def astar(start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        if node in visited and visited[node] <= g:
            continue

        visited[node] = g

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]

            if neighbor not in visited or new_g < visited[neighbor]:
                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float("inf")

start = 'A'
goal = 'F'

path, cost = astar(start, goal)

if path:
    print("Shortest path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")
