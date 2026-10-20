
from collections import deque

def valid(m, c):
    return (
        0 <= m <= 3
        and 0 <= c <= 3
        and (m == 0 or m >= c)
        and (3 - m == 0 or 3 - m >= 3 - c)
    )

def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)

    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

    queue = deque([start])
    parent = {start: None}

    while queue:
        m, c, boat = queue.popleft()
        state = (m, c, boat)

        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            nm, nc, _ = new_state

            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            if boat == 0 and (dm > m or dc > c):
                continue

            if boat == 1 and (dm > 3 - m or dc > 3 - c):
                continue

            if valid(nm, nc) and new_state not in parent:
                parent[new_state] = (m, c, boat)
                queue.append(new_state)

    return None

path = solve()

if path:
    print("Solution steps:")
    for step, (m, c, boat) in enumerate(path):
        side = "Left" if boat == 0 else "Right"
        print(
            f"Step {step}: Missionaries={m}, "
            f"Cannibals={c}, Boat={side}"
        )
else:
    print("No solution found.")
