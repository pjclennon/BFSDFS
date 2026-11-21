"""CSC 225 - Graph search starter code. Finish the TODO sections."""
from collections import deque


class Graph:
    def __init__(self):
        # A dictionary: vertex -> list of neighbors
        self.adj = {}

    def add_vertex(self, v):
        # TODO: If v is not already in the dictionary, add v with an empty list.
            if v not in self.adj:
                self.adj[v] = []

    def add_edge(self, u, v):
        # TODO: Add both vertices (if necessary).
        self.add_vertex(u)
        self.add_vertex(v)
        # TODO: Add v to u's list, unless it is already there.
        if v not in self.adj[u]:
            self.adj[u].append(v)
        # TODO: Add u to v's list, unless it is already there.
        # Assume u != v. The graph is undirected.
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def dfs(self, start):
        """Return a DFS visitation list starting at start."""
        # TODO: Make an empty visited set and an empty order list.
        visited = set()
        order = []
        # TODO: Define a recursive helper that visits a vertex and its
        #       unvisited neighbors in their stored order.
        def helper(vertex):
            visited.add(vertex)
            order.append(vertex)

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    helper(neighbor)
        # TODO: Start the helper at start and return order.
        helper(start)
        return order

        # Assume start exists in self.adj.
        pass

    def bfs(self, start):
        """Return a BFS visitation list starting at start."""
        # TODO: Make an empty visited set, an empty order list, and a queue
        #       using deque imported from collections at the top of this file.
        visited = set()
        order = []
        queue = deque()
        # TODO: Add start to the queue and mark it visited immediately.
        queue.append(start)
        visited.add(start)
        # TODO: While the queue is not empty, remove the first vertex,
        #       append it to order, and enqueue any unvisited neighbors.
        #       Mark neighbors visited when they enter the queue.
        while queue:
            vertex = queue.popleft()
            order.append(vertex)

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        # TODO: Return order.
        return order
        # Assume start exists in self.adj.
        pass
