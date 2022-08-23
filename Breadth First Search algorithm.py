#breadth first search
graph  = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H', 'I'],
    'E' : ['J'],
    'F' : ['K', 'L'],
    'G' : ['M'],
    'H' : [],
    'I' : [],
    'J' : [],   
    'K' : [],
    'L' : [],
    'M' : [] 
}
visited = []
queue = []
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
    m = queue.pop(0)
    print(m, end = "")
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("followingg is bfs:")
bfs(visited, graph, 'A')