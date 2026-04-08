import tkinter as tk
from tkinter import messagebox
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import math


# ------------------ PRIM'S ALGORITHM ------------------
def prim_mst(graph, start=0):
    visited = set()
    min_heap = [(0, start, -1)]
    mst = []
    total_cost = 0

    while min_heap:
        cost, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent != -1:
            mst.append((parent, node, cost))
            total_cost += cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor, node))

    return mst, total_cost


# ------------------ GRAPH VISUALIZATION ------------------
def show_graph(graph_edges, mst_edges, index_to_name):
    G = nx.Graph()

    for u, v, w in graph_edges:
        G.add_edge(index_to_name[u], index_to_name[v], weight=w)

    nodes = list(G.nodes())

    # Grid layout (campus style)
    grid_size = math.ceil(math.sqrt(len(nodes)))
    pos = {}

    for i, node in enumerate(nodes):
        row = i // grid_size
        col = i % grid_size
        pos[node] = (col, -row)

    plt.figure(figsize=(12, 6))

    # ---- ORIGINAL GRAPH ----
    plt.subplot(1, 2, 1)
    nx.draw(G, pos,
            with_labels=True,
            node_size=2500,
            node_color="#90caf9",
            font_size=10)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Campus Layout (All Connections)")

    # ---- MST GRAPH ----
    mst_G = nx.Graph()
    for u, v, w in mst_edges:
        mst_G.add_edge(index_to_name[u], index_to_name[v], weight=w)

    plt.subplot(1, 2, 2)
    nx.draw(mst_G, pos,
            with_labels=True,
            node_size=2500,
            node_color="#a5d6a7",
            font_size=10)

    labels = nx.get_edge_attributes(mst_G, 'weight')
    nx.draw_networkx_edge_labels(mst_G, pos, edge_labels=labels)

    plt.title("Optimized Campus Network (MST)")

    plt.tight_layout()
    plt.show()


# ------------------ MAIN FUNCTION ------------------
def generate_network():
    try:
        n = int(entry_nodes.get())

        names_input = entry_names.get().strip()
        building_names = [name.strip() for name in names_input.split(",")]

        if len(building_names) != n:
            raise ValueError("Number of buildings and names must match!")

        name_to_index = {name: i for i, name in enumerate(building_names)}
        index_to_name = {i: name for i, name in enumerate(building_names)}

        edges_input = text_edges.get("1.0", tk.END).strip().split("\n")

        graph = {i: [] for i in range(n)}
        graph_edges = []

        for edge in edges_input:
            u, v, w = edge.split()

            if u not in name_to_index or v not in name_to_index:
                raise ValueError("Invalid building name!")

            u_idx = name_to_index[u]
            v_idx = name_to_index[v]
            w = int(w)

            graph[u_idx].append((v_idx, w))
            graph[v_idx].append((u_idx, w))

            graph_edges.append((u_idx, v_idx, w))

        mst, cost = prim_mst(graph)

        # Output
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Minimum Spanning Tree:\n\n")

        for u, v, w in mst:
            result_text.insert(
                tk.END,
                f"{index_to_name[u]} -- {index_to_name[v]} (Cost: {w})\n"
            )

        result_text.insert(tk.END, f"\nTotal Cost = {cost}")

        # Show graph
        show_graph(graph_edges, mst, index_to_name)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ------------------ GUI DESIGN ------------------
root = tk.Tk()
root.title("Smart Campus Network Designer")
root.geometry("700x600")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root,
         text="Smart Campus Network Designer",
         font=("Helvetica", 18, "bold"),
         fg="white",
         bg="#1e1e2f").pack(pady=15)

# Input Frame
frame = tk.Frame(root, bg="#2c2c3e", padx=10, pady=10)
frame.pack(pady=10)

# Number of buildings
tk.Label(frame, text="Number of Buildings:",
         fg="white", bg="#2c2c3e").grid(row=0, column=0)

entry_nodes = tk.Entry(frame)
entry_nodes.grid(row=0, column=1)

# Building names
tk.Label(frame,
         text="Building Names (comma separated):",
         fg="white", bg="#2c2c3e").grid(row=1, column=0, columnspan=2, pady=5)

entry_names = tk.Entry(frame, width=30)
entry_names.grid(row=2, column=0, columnspan=2)

# Connections
tk.Label(frame,
         text="Connections (Example: Admin Library 4):",
         fg="white", bg="#2c2c3e").grid(row=3, column=0, columnspan=2, pady=5)

text_edges = tk.Text(frame, height=8, width=40)
text_edges.grid(row=4, column=0, columnspan=2)

# Button
tk.Button(root,
          text="Generate Optimal Network",
          command=generate_network,
          bg="#00c853",
          fg="white",
          font=("Arial", 12, "bold")).pack(pady=15)

# Output
output_frame = tk.Frame(root, bg="#2c2c3e")
output_frame.pack(pady=10)

tk.Label(output_frame,
         text="Output:",
         fg="white",
         bg="#2c2c3e").pack()

result_text = tk.Text(output_frame, height=10, width=60)
result_text.pack()

# Run
root.mainloop()