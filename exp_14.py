
def minimax(depth, node, maximizing, values, max_depth):
    if depth == max_depth:
        return values[node]

    if maximizing:
        return max(
            minimax(depth + 1, node * 2, False, values, max_depth),
            minimax(depth + 1, node * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node * 2, True, values, max_depth),
            minimax(depth + 1, node * 2 + 1, True, values, max_depth)
        )


values = [3, 5, 2, 9, 12, 5, 23, 23]
max_depth = 3

result = minimax(0, 0, True, values, max_depth)

print("Leaf values:", values)
print("Optimal value using Minimax:", result)
