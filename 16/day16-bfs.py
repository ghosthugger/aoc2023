import sys
def read():
    with open('input-small.txt') as f:
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

def bfs(m,q):
    global v
    energized=set()
    q.append(((0,0),">"))
    v=set()
    while(len(q)!=0):
        print(q)
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
    global q
    inp_list = read()
    pp(inp_list)
    m=[list(r) for r in inp_list]
    xs=len(m[0])
    ys=len(m)

    energized=bfs(m,q)

    for y in range(ys):
        for x in range(xs):
            if (x,y) in energized:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print(len(energized))



if __name__ =="__main__":
    main()

