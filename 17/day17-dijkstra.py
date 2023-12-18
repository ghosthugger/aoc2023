import sys
import bisect
from collections import defaultdict
import heapq



def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append([int(i) for i in l.strip()])

    return res

def pp(p):
    for l in p:
        print(l)

    print()

def dijkstra(graph, start):
    result_map = defaultdict(lambda: float('inf'))
    result_map[start] = 0

    visited = set()
    dedup=set()

    queue = [(0, start)]

    i=0
    while queue:
        weight, v = heapq.heappop(queue)
        visited.add(v)
        if i%100000==0:
            print("iter "+ str(i),end=" ")
            print(len(visited))
        i+=1
        for u, w in graph[v]:
            if u not in visited:
                result_map[u] = min(w + weight, result_map[u])
                if not (w + weight, u) in dedup:
                    heapq.heappush(queue, [w + weight, u])
                    dedup.add((w + weight, u))

    return result_map

def r90(dir):
    return ['<','>']

def child(m,x,y,dir):
    xs=len(m[0])
    ys=len(m)

    d90=None

#    if(x==0 and y==0):
#        stepsl=[(1,0) for i in range(1,4)]
#        stepsr=[(0,1) for i in range(1,4)]
#        d90='v'
#    el
    if dir=='v' or dir=='^':
        stepsl=[(1,0) for i in range(1,4)]
        stepsr=[(-1,0) for i in range(1,4)]
        d90='>'
    if dir=='<' or dir=='>':
        stepsl=[(0,-1) for i in range(1,4)]
        stepsr=[(0,1) for i in range(1,4)]
        d90='v'

    res=[]
    cost=0
    dx=0
    dy=0
    for s in stepsl:
        dx+=s[0]
        dy+=s[1]
        if x+dx<xs and x+dx>=0 and y+dy<ys and y+dy>=0:
            cost+=m[y+dy][x+dx]
            res.append(((x+dx,y+dy, d90),cost))

#    if(x==0 and y==0):
#        d90='>'
    cost=0
    dx=0
    dy=0
    for s in stepsr:
        dx+=s[0]
        dy+=s[1]
        if x+dx<xs and x+dx>=0 and y+dy<ys and y+dy>=0:
            cost+=m[y+dy][x+dx]
            res.append(((x+dx,y+dy,d90),cost))

    return res

def create_g(m):
    xs=len(m[0])
    ys=len(m)
    g={}
    dirs=['>','v']   #['<','>','^','v']
    for x in range(xs):
        for y in range(ys):
            for d in dirs:
                dests=child(m,x,y,d)
                g[(x,y,d)]=dests
    return g


def main():
    global m
    global q
    global dyn
    inp_list = read()
    pp(inp_list)

    m=inp_list
    xs=len(m[0])
    ys=len(m)

    g=create_g(m)
    print(len(g))
    print("g[(0,0,'>')]")
    print(g[(0,0,'>')])
    print("g[(0,0,'v')]")
    print(g[(0,0,'v')])
    print("g[(0,1,'>')]")
    print(g[(0,1,'>')])
    print("g[(10,10,'>')]")
    print(g[(10,10,'>')])
    r=dijkstra(g,((0,0,'v')))
    print(r)

    print(r[(xs-1,xs-1,'>')])
if __name__ =="__main__":
    main()

