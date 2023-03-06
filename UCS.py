
import queue


def ucs(start, goal, graph):
    frontier = queue.PriorityQueue()
    frontier.put((0, start))
    explored = set()
    while not frontier.empty():
        cost, node = frontier.get()
        if node == goal:
            return cost
        explored.add(node)
        for child, child_cost in graph[node].items():
            if child not in explored:
                frontier.put((cost + child_cost, child))
    return -1  # No path found


adj = {
    'Arad': {'Sibiu': 140},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

print(ucs('Arad', 'Bucharest', adj))
