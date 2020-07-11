def bfs(graph, start_node):
    visited = list()
    queue = list()
    queue.append(start_node)

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            queue.extend(graph[current])
    return visited


if __name__ == "__main__":
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']

    print(bfs(graph, 'A'))
