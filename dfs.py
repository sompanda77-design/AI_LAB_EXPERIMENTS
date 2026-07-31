def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node in visited:
            continue

        print(f"Visiting node: {current_node}")
        visited.append(current_node)

        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)

    return visited


print("--- build your graph ---")
student_graph = {}
num_edges = int(input("How many edges (connections) does your graph have? "))
print("Enter each edge separated by a space (e.g., A B):")

for _ in range(num_edges):
    u, v = input(f"Edge {_ + 1}: ").split()
    student_graph.setdefault(u, []).append(v)
    student_graph.setdefault(v, []).append(u)

start_node = input("Enter the starting node for DFS: ").strip()
visited_nodes = dfs(student_graph, start_node)
print("Visited nodes in DFS order:", visited_nodes)
