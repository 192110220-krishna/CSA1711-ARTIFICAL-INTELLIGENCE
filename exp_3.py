
from collections import deque

def water_jug(cap_a, cap_b, target):
    start = (0, 0)
    queue = deque([start])
    visited = {start: None}

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            path = []
            state = (a, b)

            while state is not None:
                path.append(state)
                state = visited[state]

            return path[::-1]

        d = min(a, cap_b - b)
        e = min(b, cap_a - a)

        next_states = [
            (cap_a, b),       # Fill jug A
            (a, cap_b),       # Fill jug B
            (0, b),           # Empty jug A
            (a, 0),           # Empty jug B
            (a - d, b + d),   # Pour A into B
            (a + e, b - e)    # Pour B into A
        ]

        for state in next_states:
            if state not in visited:
                visited[state] = (a, b)
                queue.append(state)

    return None


cap_a = int(input("Enter capacity of jug A: "))
cap_b = int(input("Enter capacity of jug B: "))
target = int(input("Enter target amount: "))

result = water_jug(cap_a, cap_b, target)

if result:
    print("\nSolution steps:")
    for step, state in enumerate(result):
        print(f"Step {step}: Jug A = {state[0]}, Jug B = {state[1]}")
else:
    print("No solution possible.")
