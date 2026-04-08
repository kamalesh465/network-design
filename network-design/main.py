from graph import Graph
from prim import prim_mst
from utils import load_graph_from_file, parse_graph, print_mst

def main():
    print("=== Minimum Cost Campus Network Design Using Prim's Algorithm ===")

    filename = "sample_input.txt"

    # Load graph
    num_nodes, graph_data = load_graph_from_file(filename)

    # Parse graph
    graph = parse_graph(num_nodes, graph_data, Graph)

    # Optional display
    graph.display()

    # Run Prim's Algorithm
    mst, total_cost = prim_mst(graph, start=0)

    # Print result
    print_mst(mst, total_cost)

if __name__ == "__main__":
    main()