import sys

def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        d,l,c=(l.strip()).split(" ")

        res.append((d,int(l)))

    return res

def fill(m,pos,v):
    if pos in v:
        return
    x,y=pos
    v.add(pos)
    if(m[y][x] == "#"):
        return
    m[y][x]="#"
    fill(m,(x+1,y),v)
    fill(m,(x-1,y),v)
    fill(m,(x,y+1),v)
    fill(m,(x,y-1),v)

def main():
    sys.setrecursionlimit(20000)
    inp_list = read()
    print(inp_list)

    xs=1000
    ys=1000

    m=[['.' for i in range(xs)] for j in range(ys)]

    x=500
    y=500
    for d,l in inp_list:
        if d=="R":
            for i in range(1,l+1):
                m[y][x+i]='#'
            x=x+i
        if d=="L":
            for i in range(1,l+1):
                m[y][x-i]='#'
            x=x-i
        if d=="D":
            for i in range(1,l+1):
                m[y+i][x]='#'
            y=y+i
        if d=="U":
            for i in range(1,l+1):
                m[y-i][x]='#'
            y=y-i

    flood=(502,501)
    v=set()
    fill(m,flood,v)

    res=0
    for x in range(xs):
        for y in range(ys):
            if m[y][x] == "#":
                res+=1

    print(res)


if __name__ =="__main__":
    main()

