"""
Problem 3: Good vs. Evil
========================
assign_good_and_evil(graph) determines if graph is bipartite (can be 2-colored
so every edge connects a 'good' and an 'evil' node).

Input:  graph - dict adjacency list: {node: [neighbors]}
Output: dict {node: 'good'|'evil'} if bipartite, else None

Time: O(V + E), Space: O(V)
"""

from collections import deque


def assign_good_and_evil(graph):
    """
    BFS-based 2-coloring. If any edge connects same-label nodes -> not bipartite.
    """
    labels = {}  # Maps each node to 'good' or 'evil'

    # Iterate over all nodes to handle disconnected components
    for node in graph:
        if node not in labels:
            # Start BFS from this unvisited node
            queue = deque([node])
            labels[node] = "good"  # Arbitrarily assign first node

            while queue:
                current = queue.popleft()
                current_label = labels[current]
                # Neighbors must have opposite label
                next_label = "evil" if current_label == "good" else "good"

                for neighbor in graph[current]:
                    if neighbor not in labels:
                        # Unvisited: assign opposite label and enqueue
                        labels[neighbor] = next_label
                        queue.append(neighbor)
                    elif labels[neighbor] == current_label:
                        # Conflict: edge between two same-label nodes -> odd cycle
                        return None

    return labels


if __name__ == "__main__":
    # Bipartite example: universities with rivalries
    example_graph = {
        "Michigan": ["Chicago"],
        "Chicago": ["Michigan", "Columbia"],
        "Columbia": ["Chicago", "UCSD"],
        "UCSD": ["Columbia"],
        "NYU": [],  # Isolated node
    }
    print(assign_good_and_evil(example_graph))
    # One possible output: {'Michigan': 'good', 'Chicago': 'evil', ...}

    # Non-bipartite: add edge Michigan-Columbia (odd cycle)
    bad_graph = {
        "Michigan": ["Chicago", "Columbia"],
        "Chicago": ["Michigan", "Columbia"],
        "Columbia": ["Chicago", "UCSD", "Michigan"],
        "UCSD": ["Columbia"],
        "NYU": [],
    }
    print(assign_good_and_evil(bad_graph))  # Expected: None
