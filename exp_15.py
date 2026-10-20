
def alpha_beta(depth, node, maximizing, alpha, beta, values):
    if depth == 3:
        return values[node]

    if maximizing:
        best = float("-inf")

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                False,
                alpha,
                beta,
                values
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float("inf")

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                True,
                alpha,
                beta,
                values
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(
    0, 0, True,
    float("-inf"),
    float("inf"),
    values
)

print("Leaf node values:", values)
print("Best value using Alpha-Beta Pruning:", result)
