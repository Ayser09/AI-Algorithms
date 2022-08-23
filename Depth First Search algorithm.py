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
visited = set()
def dfs (visited, graph, node):
  if node not in visited :
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)
print("following is the dfs :")
dfs(visited, graph, 'A')