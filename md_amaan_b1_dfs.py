graph = {
  'S' : ['A','B'],
  'A' : ['C','D'],
  'B' : ['G','H'],
  'C' : ['E','F'],
  'D' : [],
  'E' : ['K'],
  'F' : [],
  'G' : ['I'],
  'H':  [],
  'I':  [],
  'K':  [],
}
visited = []
stack = []
goal = 'K'
path = ['S']

def dfs(visited, graph, node):
    visited.append(node)
    stack.append(node)    
    while stack:
        s = stack[-1]
        if goal == s:
            break        
        neighbors = graph[s][::-1]
        unvisited_neighbors = [n for n in neighbors if n not in visited]        
        if unvisited_neighbors:
            next_node = unvisited_neighbors[0]
            visited.append(next_node)
            stack.append(next_node)
            path.append(next_node)
        else:
            stack.pop()
        
        print(f'Stack: {stack}')
        print(f'Visited: {visited}')    
    print(f'Path from {node} to {goal}: {"->".join(path)}')

dfs(visited, graph, 'S')
