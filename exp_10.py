
import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}

def astar(start, goal):
    priority_queue = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while priority_queue:
        _, g, node = heapq.heappop(priority_queue)

        if g != cost[node]:
            continue

        if node == goal:
            path = []
            current = node

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1], g

        for neighbor, weight in graph[node].items():
            new_cost = g + weight

            if new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                parent[neighbor] = node

                f = new_cost + heuristic[neighbor]
                heapq.heappush(
                    priority_queue,
                    (f, new_cost, neighbor)
                )

    return None, float('inf')


start = input("Enter start node (A-D): ").upper()
goal = input("Enter goal node (A-D): ").upper()

if start in graph and goal in graph:
    path, total_cost = astar(start, goal)

    if path:
        print("Shortest Path:", " -> ".join(path))
        print("Total Cost:", total_cost)
    else:
        print("No path found!")
else:
    print("Invalid node!")
