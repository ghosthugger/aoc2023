import sys
def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append(l.strip())

    return res

def pp(p):
    for l in p:
        print(l)

    print()
cache={}
q=[]
m=[]
v=set()

def add(pos,dir):
    global v
    global q
    x,y=pos
    if(x<0 or x>=len(m[0])):
        return

    if(y<0 or y>=len(m)):
        return

    if ((not (pos,dir) in v) and (not (pos,dir) in q)):
        q.append((pos,dir))

def bfs(m,lq):
    global v
    global q
    q=lq
    energized=set()
    v=set()
    while(len(q)!=0):
#        print(q)
        pos,dir=q.pop(0)
        x,y=pos
        energized.add(pos)
        v.add((pos,dir))
        if dir=="<":
            if m[y][x]==".":
                add((x-1,y), dir)
            elif m[y][x]=="|":
                add( (x,y-1), "^")
                add( (x,y+1), "v")
            elif m[y][x]=="-":
                add( (x-1,y), dir)
            elif m[y][x]=="/":
                add( (x,y+1), "v")
            elif m[y][x]=="\\":
                add( (x,y-1), "^")
        elif dir==">":
            if m[y][x]==".":
                add( (x+1,y), dir)
            elif m[y][x]=="|":
                add((x,y-1), "^")
                add((x,y+1), "v")
            elif m[y][x]=="-":
                add( (x+1,y), dir)
            elif m[y][x]=="/":
                add( (x,y-1), "^")
            elif m[y][x]=="\\":
                add( (x,y+1), "v")
        elif dir =="v":
            if m[y][x]==".":
                add( (x,y+1), dir)
            elif m[y][x]=="|":
                add( (x,y+1), dir)
            elif m[y][x]=="-":
                add((x-1,y), "<")
                add((x+1,y), ">")
            elif m[y][x]=="/":
                add( (x-1,y), "<")
            elif m[y][x]=="\\":
                add( (x+1,y), ">")
        elif dir =="^":
            if m[y][x]==".":
                add( (x,y-1), dir)
            elif m[y][x]=="|":
                add( (x,y-1), dir)
            elif m[y][x]=="-":
                add((x-1,y), "<")
                add((x+1,y), ">")
            elif m[y][x]=="/":
                add( (x+1,y), ">")
            elif m[y][x]=="\\":
                add( (x-1,y), "<")
    return energized

def main():
    global m
    inp_list = read()
    pp(inp_list)
    m=[list(r) for r in inp_list]
    xs=len(m[0])
    ys=len(m)

    maxe=0

    for x in range(xs):
        print("x" + str(x))
        energized=bfs(m,[((x,0),"v")])
        maxe=max(len(energized), maxe)
        energized=bfs(m,[((x,ys-1),"^")])
        maxe=max(len(energized), maxe)

    for y in range(ys):
        print("y" + str(y))
        energized=bfs(m,[((0,y),">")])
        maxe=max(len(energized), maxe)
        energized=bfs(m,[((xs-1,y),"<")])
        maxe=max(len(energized), maxe)

    print(maxe)

if __name__ =="__main__":
    main()

