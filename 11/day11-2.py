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

    xempty=[]
    for y in range(maxy):
        found=False
        for x in range (maxx):
            if(m[y][x]=='#'):
                found=True
        if(not found):
            xempty.append(y)

    yempty.sort(reverse=True)
    xempty.sort(reverse=True)

    # for y in range(maxy):
    #     for e in yempty:
    #         m[y].insert(e,'.')
    # maxx=len(inp_list[0])
    # maxy=len(inp_list)
    #
    # print("m expanded")
    # for y in range(maxy):
    #     for x in range(maxx):
    #         print(m[y][x], end='')
    #     print("")
    # print("end m expanded")

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


    #yempty.sort(reverse=True)
    #xempty.sort(reverse=True)

    factor=1000000-1
    res=0
    for g1,g2 in pairs:
        x0,y0=g1
        x1,y1=g2
        res+=abs(x0-x1)+abs(y0-y1)
        for xw in yempty:
            if((xw>x1 and xw<x0) or (xw>x0 and xw<x1)):
                res+=factor
        for yw in xempty:
            if((yw>y1 and yw<y0) or (yw>y0 and yw<y1)):
                res+=factor

    print(res)



if __name__ =="__main__":
    main()

