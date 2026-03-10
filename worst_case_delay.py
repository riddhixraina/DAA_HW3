"""
Problem 4(b): Network Latency - Worst Case Delay
================================================
worst_case_delay(graph) computes the maximum shortest-path length between
any pair of nodes (graph diameter) in an unweighted connected graph.

Input:  graph - dict adjacency list: {node: [neighbors]}
Output: Integer: maximum BFS distance over all pairs

Time: O(V(V + E)), Space: O(V)
"""

from collections import deque


def bfs_distances(graph, start):
    """
    BFS from start; returns dict mapping each reachable node to its
    shortest-path distance from start.
    """
    dist = {start: 0}
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def worst_case_delay(graph):
    """
    All-pairs shortest paths via BFS from each node.
    Returns max distance (graph diameter).
    """
    nodes = list(graph.keys())
    global_max = 0

    for node in nodes:
        # BFS from this node to get distances to all others
        distances = bfs_distances(graph, node)
        if distances:
            current_max = max(distances.values())
            global_max = max(global_max, current_max)

    return global_max


if __name__ == "__main__":
    # Counterexample graph from Part 3(a): path A-B-C-D-E with X connected to B,D
    graph = {
        "A": ["B"],
        "B": ["A", "C", "X"],
        "C": ["B", "D"],
        "D": ["C", "E", "X"],
        "E": ["D"],
        "X": ["B", "D"],
    }
    print(worst_case_delay(graph))  # Expected: 4 (path A-B-C-D-E)

    # Single node
    print(worst_case_delay({"A": []}))  # Expected: 0
