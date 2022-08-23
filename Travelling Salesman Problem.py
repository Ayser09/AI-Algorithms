from itertools import permutations
from json.encoder import INFINITY
def tsp(nodes,cost, source):
    vertices=[i for i in nodes if i!=source]
    possible_paths = permutations(vertices)
    route=[]
    min_cost = INFINITY
    for path in possible_paths:
        n = source
        current_path_cost=0
        for node in path:
            current_path_cost += cost[n][node]
            n = node
        current_path_cost += cost[n][source]
        if min_cost>current_path_cost:
            min_cost=current_path_cost
            route=list(path)
    route.append(source)
    route.insert(0,source)
    return route, min_cost
nodes=[0,1,2,3]
cost=[[0,10,15,20],
      [10,0,35,25],
      [15,35,0,30],
      [20,25,30,0]]
route, min_cost = tsp(nodes,cost,0)
print("Path - ",*route,"\nMinimum cost - ", min_cost)