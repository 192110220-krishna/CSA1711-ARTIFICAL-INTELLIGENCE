
from itertools import permutations

# Distance matrix between four cities: A, B, C, D
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = ['A', 'B', 'C', 'D']
n = len(cities)

min_cost = float('inf')
best_path = None

# Keep city A as the starting city
for order in permutations(range(1, n)):
    path = (0,) + order + (0,)
    cost = 0

    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Shortest Tour:")
print(" -> ".join(cities[i] for i in best_path))
print("Minimum Cost:", min_cost)
