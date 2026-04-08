def load_graph_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    num_nodes = int(lines[0].strip())
    graph_data = lines[1:]

    return num_nodes, graph_data


def parse_graph(num_nodes, graph_data, GraphClass):
    graph = GraphClass(num_nodes)

    for line in graph_data:
        u, v, w = map(int, line.strip().split())
        graph.add_edge(u, v, w)

    return graph


def print_mst(mst, cost):
    print("\nMinimum Spanning Tree (Using Prim's Algorithm):")
    for u, v, w in mst:
        print(f"{u} -- {v}  (Cost: {w})")
    print(f"\nTotal Minimum Cost = {cost}")