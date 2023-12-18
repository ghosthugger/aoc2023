import sys
import bisect

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

cache={}
q=[]
m=[]
v=set()
dyn=[]

def add(pos,dir,streak,pathloss,way):
    global v
    global q
    global m
    global dyn
    xs=len(m[0])
    ys=len(m)
    x,y=pos
    if(x<0 or x>=len(m[0])):
        return

    if(y<0 or y>=len(m)):
        return

    md=((xs-x-1) +(ys-y-1))

#    if(x==11 and y==12):
#        print("end")

    # remain=[]
    # for i in range(x,xs):
    #     for j in range(y,ys):
    #         remain.append(m[j][i])
    #
    # remain.remove(m[ys-1][xs-1])
    # remain.sort()
    # est=sum(remain[:md-1])+m[ys-1][xs-1]

    est=dyn[y][x]

    if ((not (pos,dir,streak) in v)): # and (not (pos,dir,streak,pathloss+m[y][x],est,[]) in q)):
        i=0
        while i<len(q) and q[i][3]+q[i][4]<pathloss+m[y][x]+est:
            i+=1
        q.insert(i,(pos,dir,streak,pathloss+m[y][x],est,[])) #way+[pos]))

def bfs(m,q):
    global v
    global dyn
    q.append(((0,0),">",0,0,0,[]))
    q.append(((0,0),"v",0,0,0,[]))
    v=set()
    loss=0
    xs=len(m[0])
    ys=len(m)
    i=0
    while(len(q)!=0):
        if i%1000==0:
            print(len(q))
            print(q[:3])
            print(q[-3:])
        i+=1
        pos,dir,streak,pathloss,estimate,way=q.pop(0)
        x,y=pos

        if(x==len(m[0])-1 and y==len(m)-1):
            loss=pathloss
            lossway=way
            break

        if(dir==">"):
            if streak<2:
                add((x+1,y),">",streak+1,pathloss,way)
            add((x,y-1),"^",0,pathloss,way)
            add((x,y+1),"v",0,pathloss,way)
        elif(dir=="v"):
            if streak<2:
                add((x,y+1),"v",streak+1,pathloss,way)
            add((x-1,y),"<",0,pathloss,way)
            add((x+1,y),">",0,pathloss,way)
        elif(dir=="<"):
            if streak<2:
                add((x-1,y),"<",streak+1,pathloss,way)
            add((x,y-1),"^",0,pathloss,way)
            add((x,y+1),"v",0,pathloss,way)
        elif(dir=="^"):
            if streak<2:
                add((x,y-1),"^",streak+1,pathloss,way)
            add((x+1,y),">",0,pathloss,way)
            add((x-1,y),"<",0,pathloss,way)

#        q.sort(key=lambda x:x[3]+x[4])
        v.add((pos,dir,streak))

    print(lossway)
    return lossway, loss

def minstep(dyn,m,x,y):
    xs=len(m[0])
    ys=len(m)

    res=m[y][x]

    minpath=100000000000
    if y<ys-1:
        minpath=min(minpath,dyn[y+1][x])
    if x<xs-1:
        minpath=min(minpath,dyn[y][x+1])

    if minpath != 100000000000:
        res+=minpath
    return res


def recest(dyn,m,x,y):
    xs=len(m[0])
    ys=len(m)
    if(x>xs-1):
        return 10000

    if(y>ys-1):
        return 10000

    if(dyn[y][x]!=-1):
        return dyn[y][x]

    if x==xs-1 and y==ys-1:
        dyn[y][x]=0
        return dyn[y][x]
    else:
        r=recest(dyn,m,x+1,y)
        d=recest(dyn,m,x,y+1)
        res=m[y][x] + min(r,d)
        dyn[y][x]=res
    return res

def main():
    global m
    global q
    global dyn
    inp_list = read()
    pp(inp_list)

    m=inp_list
    xs=len(m[0])
    ys=len(m)

    dyn=[[-1 for i in range(xs)] for j in range(ys)]
    recest(dyn,m,0,0)

    print(dyn)


#    for d in range(xs,0,-1):
#        for e in range(xs-1,d-1,-1):
#            dyn[e][d]=minstep(dyn,m,d,e)

    print("dyn")
    for y in range(ys):
        for x in range(xs):
            print('{0:03}'.format(dyn[y][x]), end=",")
        print()

    lossway,loss=bfs(m,q)
#    lossway,loss=[],17

    print("loss")
    print(loss)

    for y in range(ys):
        for x in range(xs):
            if (x,y) in lossway:
                print("*", end="")
            else:
                print(m[y][x], end="")
        print()

if __name__ =="__main__":
    main()

