graph = {
  'S' : ['A','B'],
  'F' : [],
  'A' : ['C','D'],
  'B' : ['G','H'],
  'E' : ['K'],
  'C' : ['E','F'],
  'D' : [],
  'G' : ['I'],
  'I':  [],
  'K':  [],
  'H':  []
}

visited = []
queue = []
path=['S']
goal = 'K'

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print(f'Visited: {visited}')
    print(f'Queue: {queue}')
    print(s, end=" ")
    if goal == s:
      break

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        path.append(neighbour)
  print(f'\nPath from {node} to {goal}: {"->".join(path)}')
                    

bfs(visited, graph, 'S')
