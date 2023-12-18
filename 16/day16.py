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

def dfs(m, pos, dir, v):
    sys.setrecursionlimit(20000)

    el=(pos,dir)
    if el in cache:
        return cache[el]

    energized=set()

    x,y=pos

    if pos==(6,6):
        print("pass")

    if(x<0 or x>=len(m[0])):
        return set()

    if(y<0 or y>=len(m)):
        return set()

    if ((x,y), dir) in v:
        return  set()

    v.append((pos, dir))

    energized.add(pos)

    if dir=="<":
        if m[y][x]==".":
            return energized | dfs(m, (x-1,y), dir, v)
        elif m[y][x]=="|":
            e1=dfs(m, (x,y-1), "^", v.copy())
            e2=dfs(m, (x,y+1), "v", v.copy())
            res= energized | e1 | e2
            el=(pos,dir)
            cache[el]=res
            return res
        elif m[y][x]=="-":
            return energized | dfs(m, (x-1,y), dir, v)
        elif m[y][x]=="/":
            return energized | dfs(m, (x,y+1), "v", v)
        elif m[y][x]=="\\":
            return energized | dfs(m, (x,y-1), "^", v)
    elif dir==">":
        if m[y][x]==".":
            return energized | dfs(m, (x+1,y), dir, v)
        elif m[y][x]=="|":
            e1=dfs(m, (x,y-1), "^", v.copy())
            e2=dfs(m, (x,y+1), "v", v.copy())
            res= energized | e1 | e2
            el=(pos,dir)
            cache[el]=res
            return res
        elif m[y][x]=="-":
            return energized | dfs(m, (x+1,y), dir, v)
        elif m[y][x]=="/":
            return energized | dfs(m, (x,y-1), "^", v)
        elif m[y][x]=="\\":
            return energized | dfs(m, (x,y+1), "v", v)
    elif dir =="v":
        if m[y][x]==".":
            return energized | dfs(m, (x,y+1), dir, v)
        elif m[y][x]=="|":
            return energized | dfs(m, (x,y+1), dir, v)
        elif m[y][x]=="-":
            e1=dfs(m, (x-1,y), "<", v.copy())
            e2=dfs(m, (x+1,y), ">", v.copy())
            res= energized | e1 | e2
            el=(pos,dir)
            cache[el]=res
            return res
        elif m[y][x]=="/":
            return energized | dfs(m, (x-1,y), "<", v)
        elif m[y][x]=="\\":
            return energized | dfs(m, (x+1,y), ">", v)
    elif dir =="^":
        if m[y][x]==".":
            return energized | dfs(m, (x,y-1), dir, v)
        elif m[y][x]=="|":
            return energized | dfs(m, (x,y-1), dir, v)
        elif m[y][x]=="-":
            e1=dfs(m, (x-1,y), "<", v.copy())
            e2=dfs(m, (x+1,y), ">", v.copy())
            res= energized | e1 | e2
            el=(pos,dir)
            cache[el]=res
            return res
        elif m[y][x]=="/":
            return energized | dfs(m, (x+1,y), ">", v)
        elif m[y][x]=="\\":
            return energized | dfs(m, (x-1,y), "<", v)

    assert(False)
    return energized

def main():
    inp_list = read()
    pp(inp_list)
    m=[list(r) for r in inp_list]
    xs=len(m[0])
    ys=len(m)

    energized=dfs(m,(0,0),">",[])

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

