# TASK 01 PART(B)
from collections import deque
# adj is adjacent list representation of graphs
# V is no. of sourcees in graph
# def bfsOfGraph(V, adj):

#     bfs_traversal = []
#     vis = [False]*V

#     for i in range(V):
#         # To check if already visited
#         if (vis[i] == False):
#             q = []
#             q.append(i)
#             vis[i] = True

#             # BFS starting from ith node
#             while (len(q) > 0):
#                 node = q.pop(0)

#                 bfs_traversal.append(node)
#                 # for adjacent nodes of source
#                 for it in adj[node]:
#                     if (vis[it] == False):
#                         vis[it] = True
#                         q.append(it)

#     return bfs_traversal

# DFS function that takes in a graph, a starting source, and a visited set


def dfs(graph, source, visited):
    # Mark the current source as visited
    visited.add(source)
    print(source)

    # Recur for all the vertices adjacent to this source
    for neighbor in graph[source]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# BFS function that takes in a graph, a starting vertex, and a visited set
def bfs(graph, start, visited):
    # Create a queue for BFS
    queue = deque([start])
    visited.add(start)

    # Loop through the queue until it's empty
    while queue:
        # Dequeue a vertex from the queue and print it
        vertex = queue.popleft()
        print(vertex)

        # Enqueue all adjacent vertices that haven't been visited
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


adj = {0: [1, 2, 3, 5],
       1: [0, 3, 4],
       2: [0, 3],
       3: [0, 1, 2, 4],
       4: [1, 3],
       5: [0]}

visited = set()
# dfs(adj, 0, visited)
bfs(adj, 0, visited)
