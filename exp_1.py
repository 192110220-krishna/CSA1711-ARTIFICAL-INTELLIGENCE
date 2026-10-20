import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            goal_pos = value - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)

    return distance

def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    neighbors = []

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors

def solve(start):
    pq = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        _, g, state = heapq.heappop(pq)

        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        if g != cost[state]:
            continue

        for neighbor in get_neighbors(state):
            new_cost = g + 1

            if new_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_cost
                parent[neighbor] = state

                heapq.heappush(
                    pq,
                    (new_cost + heuristic(neighbor),
                     new_cost, neighbor)
                )

    return None

start = tuple(map(
    int, input("Enter 9 numbers (0 for blank): ").split()
))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input!")
else:
    path = solve(start)

    if path:
        for step, state in enumerate(path):
            print("\nStep", step)
            for i in range(0, 9, 3):
                print(state[i:i+3])
    else:
        print("No solution found!")
