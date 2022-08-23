
graph = {'A':['B','C','D'],
        'B':['A','E'],
        'C':['A','E','F'],
        'D':['F','A'],
        'E':['B','C','K'],
        'F':['D','C','G'],
        'G':['K','F','H'],
        'H':['G','I'],
        'J':['G','I'],
        'K':['E','G']}
heuristic = {'A':40, 'B':32, 'C':25, 'D':35, 'E':19, 'F':17, 'G':0, 'K':10}
open = []
closed=[]
def find_min(list):
    min=list[0]
    for i in list:
        if heuristic[i]<heuristic[min]:
            min=i        
    return min, heuristic[min]

def hill_climbing(graph, heuristic, node, open, closed):
    if len(open)==0:
        open.append(node)
       
    open.remove(node)
    closed.append(node)
    
    for children in graph[node]:
        if children not in closed and children not in open:
            open.append(children)
    prev_value=heuristic[node]
    ele,value = find_min(open)
    
    if value==0:
        closed.append(ele)
        open.remove(ele)
        print("Solution found")
        print(closed)
        return
    elif value>=prev_value:
        print(closed)
        print("No solution found")
        return
    else:
        prev_value=value
        hill_climbing(graph, heuristic, ele,open, closed)      
hill_climbing(graph,heuristic, 'A',open,closed)
print("OPEN LIST:", open)
print("CLOSED LIST:", closed)  
print("path:", *closed)
 
