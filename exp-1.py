from heapq import heappush, heappop

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_pos = goal.index(tile)
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def get_neighbors(state):
    zero = state.index(0)
    row, col = zero // 3, zero % 3
    neighbors = []

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            new_state = list(state)

            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, [start]))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heappush(
                    pq,
                    (g + 1 + heuristic(neighbor),
                     g + 1,
                     neighbor,
                     path + [neighbor])
                )

    return None

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

path = solve(start)

if path:
    for step, state in enumerate(path):
        print("Step", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found")
