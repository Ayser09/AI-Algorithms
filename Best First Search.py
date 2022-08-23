
graph={'S':['A','B'],
        'A':['C','D'],
        'B':['E','F'],
        'E':['H'],
        'F':['I','G']}
heuristic={'S':13,'A':12,'B':4,'C':7,'D':3,'E':8,'F':2,'H':4,'I':9,'G':0}
#heuristic = {'A':40, 'B':32, 'C':25, 'D':35, 'E':19, 'F':17, 'G':0, 'K':10, 'H':-1,'I':-1,'J':-1}

open = []
closed=[]

def find_min(list):
    min=list[0]
    for i in list:
        if  heuristic[i]==0:
            min=i
        elif heuristic[i]<heuristic[min]:
            min=i
    return min, heuristic[min]
visited=[]
def best_first(graph, heuristic, node, open, closed):
    
    #if node not in visited:
    open.append(node)
    visited.append(node)
    i=0
    closed.append(node)
    node=open.pop()
    
    for children in graph[node]:
        if children not in visited:
            visited.append(children)
            open.insert(i,children)
            i+=1
    
    ele,value = find_min(open)
    if value==0:
        closed.append(ele)
        print(closed)
        return
    else:
        #print(open)
        #print("-->",closed)
        best_first(graph, heuristic, ele,open, closed)
        
best_first(graph,heuristic, 'S',open,closed)
print("OPEN LIST:", open)
print("CLOSED LIST:", closed)  
print("path:", *closed)
