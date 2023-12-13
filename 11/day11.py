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
        if(l.strip().find("#")==-1):   # double
            res.append(row)
            row=[]
            for c in l.strip():
                row.append(c)


        res.append(row)

    return res


def path(m,g1,g2):
    res=0

    x0,y0=g1
    x1,y1=g2
    xdist=abs(x1-x0)
    ydist=-(y1-y0)
    xstep=-1
    if(x0<x1):
        xstep=1
    ystep=-1
    if(y0<y1):
        ystep=1
    error=xdist+ydist

    if(m[y0][x0]=="."):
        m[y0][x0]="*"
    res+=1

    while ((x0 != x1) or (y0 != y1)):
        if ((2*error - ydist) > (xdist - 2*error)):
            # horizontal step
            error += ydist
            x0 += xstep
        else:
            # vertical step
            error += xdist
            y0 += ystep

        if(m[y0][x0]=="."):
            m[y0][x0]="*"
        res+=1

    return res-1

def main():
    inp_list = read()
    print(inp_list)

    maxx=len(inp_list[0])
    maxy=len(inp_list)
    m=inp_list

    yempty=[]
    for x in range(maxx):
        found=False
        for y in range (maxy):
            if(m[y][x]=='#'):
                found=True
        if(not found):
            yempty.append(x)

    yempty.sort(reverse=True)
    for y in range(maxy):
        for e in yempty:
            m[y].insert(e,'.')
    maxx=len(inp_list[0])
    maxy=len(inp_list)

    print("m expanded")
    for y in range(maxy):
        for x in range(maxx):
            print(m[y][x], end='')
        print("")
    print("end m expanded")

    gals=[]
    num=1
    for y in range(maxy):
        for x in range(maxx):
            if(m[y][x]=="#"):
                gals.append((x,y))
                m[y][x]=str(num)
                num+=1

    print("m expanded n numbered")
    for y in range(maxy):
        for x in range(maxx):
            print(m[y][x], end='')
        print("")
    print("end m expanded n numbered")

    pairs_set=set()
    for i in gals:
        for j in gals:
            if not (j,i) in pairs_set and i!=j:
                pairs_set.add((i,j))

    pairs=list(pairs_set)

    print(len(pairs))

    print(pairs)


    # res=0
    # for g1,g2 in pairs:
    #     mc=[x[:] for x in m]
    #     res+=path(mc,g1,g2)
    #
    #     # print("m line")
    #     # for y in range(maxy):
    #     #     for x in range(maxx):
    #     #         print(mc[y][x], end='')
    #     #     print("")
    #     # print("end m line")
    #
    # print(res)

    res=0
    for g1,g2 in pairs:
        x0,y0=g1
        x1,y1=g2
        res+=abs(x0-x1)+abs(y0-y1)
    print(res)



if __name__ =="__main__":
    main()

