import sys
import math
def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        row=[]
        for c in l.strip():
            row.append(c)

        res.append(row)

    return res

maxx=None
maxy=None
m=None
v=set()
dists={}

def pos(x,y):
    global maxx
    global maxy
    global m

    if(x>maxx or x<0):
        return "."
    if(y>maxy or y<0):
        return "."

    return m[y][x]

def childs(x,y):
    dirs={'|':[(0,1),(0,-1)], '-':[(-1,0),(1,0)],
          'L':[(0,-1),(1,0)], 'J':[(0,-1),(-1,0)], '7':[(0,1),(-1,0)],
          'F':[(0,1), (1,0)], '.':[],
          'S':[(1,0),(-1,0),(0,1),(0,-1)]}

    res=[]
    for cx,cy in dirs[pos(x,y)]:
        res.append((x+cx,y+cy))
    return res

def dfs(node, d):
    global maxx
    global maxy
    global m
    global v
    global dists

    xn,yn=node
    if(pos(xn,yn) == 'S'):
        print("Found it")
        return xn,yn

    v.add((xn,yn))
    dists[(xn,yn)] = d
    for cx,cy in childs(xn,yn):
        if(not (cx,cy) in v):
            return dfs((cx,cy), d+1)


    return None

def main():
    sys.setrecursionlimit(20000)
    global maxx
    global maxy
    global m
    global dists
    global v

    inp_list = read()
    print(inp_list)

    maxx=len(inp_list[0])
    maxy=len(inp_list)
    m=inp_list

    sx=None
    sy=None
    for x in range(maxx):
        for y in range(maxy):
            if(m[y][x]=="S"):
                sx=x
                sy=y
    print(maxx)
    print(maxy)
    print(sx)
    print(sy)

    start_dir=[]
    for cx,cy in childs(sx,sy):
        start_dir.append(dfs((cx,cy), 1))

    print("Start dirs")
    print(start_dir)



    v=set()
    dists={}
    for cx,cy in [childs(sx,sy)[0]]:
        start_dir.append(dfs((cx,cy), 1))

    print("distances")
    for y in range(maxy):
        for x in range(maxx):
            if((x,y) in dists):
                print(dists[(x,y)], end="")
            else:
                print(",", end="")
        print("")

    print("end dists")

    maxd=0
    maxnode=None
    for n,d in dists.items():
        oldmax=maxd
        maxd=max(maxd,d)
        if(oldmax!=maxd):
            maxnode=n

    print(maxd)
    print(maxnode)
    print(len(dists))

    print(math.ceil(maxd/2))

if __name__ =="__main__":
    main()

