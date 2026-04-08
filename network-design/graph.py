class Graph:
    def __init__(self, num_nodes):   # ✅ DOUBLE UNDERSCORE
        self.V = num_nodes
        self.graph = {i: [] for i in range(num_nodes)}

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # undirected graph

    def display(self):
        print("\nGraph Representation (Adjacency List):")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")