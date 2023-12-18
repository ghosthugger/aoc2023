import sys
import math

def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        d,l,c=(l.strip()).split(" ")

        res.append((d,int(l),c))

    return res


def shoelace_formula(polygonBoundary, absoluteValue = True):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    if absoluteValue:
        return abs(sum(l) / 2)
    else:
        return sum(l) / 2

def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])


def main():
    sys.setrecursionlimit(20000)
    inp_list = read()
    print(inp_list)

    decoded=[]
    dir={0:"R",1:"D",2:"L",3:"U"}
    for id,il,ic in inp_list:
        h=ic.strip("(#)")
        l=int(h[:-1],16)
        d=dir[int(h[-1])]

        decoded.append((d,l))

    print(decoded)

    bound=[]
    x=0
    y=0
    outline=0
    #bound.append((0,0))
    for d,l in decoded:
        if d=="R":
            x=x+l
            bound.append((x,y))
            outline+=l
        if d=="L":
            x=x-l
            bound.append((x,y))
#            outline+=l
        if d=="D":
            y=y+l
            bound.append((x,y))
#            outline+=l
        if d=="U":
            y=y-l
            bound.append((x,y))
            outline+=l

    print("last ",end="")
    print(bound[-1])
    bound.reverse()
    print(bound)

    res=area(bound)+outline+1 # +1 to count first point

    print(res)
if __name__ =="__main__":
    main()

