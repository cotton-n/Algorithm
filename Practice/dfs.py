def dfs(graph, start_node):
    visited = list()
    stack = list()
    stack.append(start_node)

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack.extend(graph[current])
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

    print(dfs(graph, 'A'))
