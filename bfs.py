def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(f"Visiting node: {current_node}")
            visited.append(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited

print("---build your graph---")
student_graph = {}
num_edges = int(input("how many edges (connections) does your graph have? "))   
print("Enter each edge separated by a space (e.g., A B for an edge between A and B):")
for _ in range(num_edges):
    u,v = input(f"Edge {_+1}: ").split()

    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []

    student_graph[u].append(v)
    student_graph[v].append(u)

start_node = input("Enter the starting node for BFS: ")
visited_nodes = bfs(student_graph, start_node)
print("Visited nodes in BFS order:", visited_nodes)
