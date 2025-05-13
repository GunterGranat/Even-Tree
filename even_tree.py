def evenForest(t_nodes, t_edges, t_from, t_to):
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for u, v in zip(t_from, t_to):
        graph[u].append(v)
        graph[v].append(u)

    # Initialize visited and counter
    visited = [False] * (t_nodes + 1)
    removable_edges = 0

    # DFS to count subtree sizes
    def dfs(node):
        nonlocal removable_edges
        visited[node] = True
        size = 1  # Count this node

        for neighbor in graph[node]:
            if not visited[neighbor]:
                subtree_size = dfs(neighbor)
                if subtree_size % 2 == 0:
                    # Can remove the edge to this subtree
                    removable_edges += 1
                else:
                    size += subtree_size
        return size

    dfs(1)
    return removable_edges
