
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']
assignment = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def solve():
    if len(assignment) == len(graph):
        return True

    region = next(r for r in graph if r not in assignment)

    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False

if solve():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution found!")
