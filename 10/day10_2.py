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
inout={}


def pos(x,y):
    global maxx
    global maxy
    global m

    if(x>=maxx or x<0):
        return "."
    if(y>=maxy or y<0):
        return "."

    return m[y][x]

def childsn(node):
    return childs(node[0], node[1])

def childs(x,y):
    dirs={'|':[(0,1),(0,-1)], '-':[(-1,0),(1,0)],
          'L':[(0,-1),(1,0)], 'J':[(0,-1),(-1,0)], '7':[(0,1),(-1,0)],
          'F':[(0,1), (1,0)], '.':[],
          'S':[(1,0),(0,-1)]} #[(-1,0),(0,-1)]} #

    res=[]
    for cx,cy in dirs[pos(x,y)]:
        res.append((x+cx,y+cy))
    return res

def intersect(lst1, lst2):
    return len(list(set(lst1) & set(lst2))) > 0

def sneak(x,y):
    tl=(x,y)
    tr=(x+1,y)
    ll=(x,y+1)
    lr=(x+1,y+1)

    res=[]
    if not (intersect([tl], childsn(tr)) and intersect(childsn(tl), [tr])):
        res.append((x,y-1))
    if not (intersect([tl], childsn(ll)) and intersect(childsn(tl), [ll])):
        res.append((x-1,y))
    if not (intersect([ll], childsn(lr)) and intersect(childsn(ll), [lr])):
        res.append((x,y+1))
    if not (intersect([tr], childsn(lr)) and intersect(childsn(tr), [lr])):
        res.append((x+1,y))

    return res

def make_m(mp):
    m=[]
    for l in mp:
        mr=[]
        for c in l:
            mr.append(c)
        m.append(mr)
    return m

def test_sneak(lm, ways):
    global maxx
    global maxy
    global m

    m=make_m(lm);
    maxx=len(m[0])
    maxy=len(m)
    assert(len(sneak(1,1))== ways)

def test_sneaks():
    global maxx
    global maxy
    global m

    #test - up
    test_sneak(["...",
                ".-|",
                "..."], 4)

    test_sneak(["...",
                ".--",
                "..."], 3)

    test_sneak(["...",
                ".-L",
                "..."], 4)

    test_sneak(["...",
                ".-J",
                "..."], 3)

    test_sneak(["...",
                ".-7",
                "..."], 3)

    test_sneak(["...",
                ".-F",
                "..."], 4)

    test_sneak(["...",
                ".|-",
                "..."], 4)

    test_sneak(["...",
                ".L-",
                "..."], 3)

    test_sneak(["...",
                ".J-",
                "..."], 4)

    test_sneak(["...",
                ".7-",
                "..."], 4)

    test_sneak(["...",
                ".F-",
                "..."], 3)


    #test - down
    test_sneak(["...",
                "...",
                ".-|"], 4)

    test_sneak(["...",
                "...",
                ".--"], 3)

    test_sneak(["...",
                "...",
                ".-L"], 4)

    test_sneak(["...",
                "...",
                ".-J"], 3)

    test_sneak(["...",
                "...",
                ".-7"], 3)

    test_sneak(["...",
                "...",
                ".-F"], 4)

    test_sneak(["...",
                "...",
                ".|-"], 4)

    test_sneak(["...",
                "...",
                ".L-"], 3)

    test_sneak(["...",
                "...",
                ".J-"], 4)





    test_sneak(["...",
                ".7-",
                "..."], 4)

    test_sneak(["...",
                ".F-",
                "..."], 3)





    test_sneak(["...",
                ".|.",
                ".|."], 3)

    test_sneak(["...",
                ".|.",
                ".J."], 3)

    test_sneak(["...",
                "..F",
                "..L"], 3)


def dfs(node, d):
    global maxx
    global maxy
    global m
    global v
    global dists

    xn,yn=node
    v.add((xn,yn))
    dists[(xn,yn)] = d

    if(pos(xn,yn) == 'S'):
        print("Found it")
        return [(xn,yn)]

    for cx,cy in childs(xn,yn):
        if(not ((cx,cy) in v
        or (d<3 and pos(cx,cy)=='S'))):
            dfsres=dfs((cx,cy), d+1)
            if dfsres != None:
                return [node] + dfsres


    return None


def sneak_dfs(node, d):
    global maxx
    global maxy
    global m
    global inout

    xn,yn=node
    if((xn,yn) in inout):
        return inout[(xn,yn)]

    if((xn,yn) in v):
       return None

    v.add((xn,yn))

    if(xn<0 or xn>maxx or yn<0 or yn>maxy):
        return "O"

    res=None
    for cx,cy in sneak(xn,yn):
        lres=sneak_dfs((cx,cy), d+1)
        if(lres=="O"):
            inout[(xn,yn)] = "O"
            return "O"

    return res

def sneak_dfs_start(node, d):
    global v
    v=set()
    xn,yn=node
    res=sneak_dfs(node, d)
    if res==None:
        inout[(xn,yn)] = "I"
        return "I"
    return res


def main():
    sys.setrecursionlimit(20000)
    global maxx
    global maxy
    global m
    global dists
    global v
    global inout

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
    start_childs=childs(sx,sy)
    for cx,cy in start_childs:
        v=set()
        start_dir.append(dfs((cx,cy), 1))

    v=set()
    dists={}
    path=[]
    for cx,cy in [childs(sx,sy)[0]]:
        path.append(dfs((cx,cy), 1))

    path_set=set(path[0])
    m2=[]
    print("m2")
    for y in range(maxy):
        m2row=[]
        for x in range(maxx):
            if((x,y) in path_set):
                print(m[y][x], end="")
                m2row.append(m[y][x])
            else:
                m2row.append(".")
                print(".", end="")
        print("")
        m2.append(m2row)
    print("end m2")

    m=m2 # clean map

    inout={}
    v=set()
    for x in range(maxx):
        for y in range(maxy):
            v=set()
            if(not (x,y) in path_set):
                sneak_dfs_start((x,y), 1)


    print("inout")
    for y in range(maxy):
        for x in range(maxx):
            if((x,y) in inout):
                print(inout[(x,y)], end="")
            else:
                print('.', end="")
        print("")
    print("end inout")



    num_is=0
    print("inout")
    for y in range(maxy):
        for x in range(maxx):
            if((x,y) in inout):
                if(m[y][x] == '.'):
                    print(inout[(x,y)], end="")
                    if(inout[(x,y)]=='I'):
                        num_is+=1
                else:
                    print(m[y][x], end="")
        print("")
    print("end inout")

    num_is=0
    num_os=0
    print("inout2")
    for y in range(maxy):
        for x in range(maxx):
            if(not (x,y) in path_set):
                if(inout[(x,y)]=='I'):
                    num_is+=1
                if(inout[(x,y)]=='O'):
                    num_os+=1
    print("end inout2")

    print("num_is:", end="")
    print(num_is)
    print("num_os:", end="")
    print(num_os)
    print("len path:", end="")
    print(len(path_set))


if __name__ =="__main__":
    #test_sneaks()
    main()

#722 is wrong
