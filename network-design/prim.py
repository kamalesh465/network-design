import heapq

def prim_mst(graph_obj, start=0):
    graph = graph_obj.graph
    visited = set()
    min_heap = [(0, start, -1)]  # (cost, current_node, parent)
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