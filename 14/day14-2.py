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

def roll(m):
    ys=len(m)
    xs=len(m[0])
    for x in range(xs):
        moved=True
        while moved:
#            pp(m)
            moved=False
            lowest_slot=0

            while lowest_slot!=None and lowest_slot<ys:
                for y in range(lowest_slot, ys):
                    if(m[y][x]=="#" or m[y][x]=="O"):
                        lowest_slot=None

                    if(m[y][x]=="."):
                        lowest_slot=y
                        break

                if lowest_slot!=None and y<ys:
                    found=False
                    for ym in range(lowest_slot,ys):
                        if(m[ym][x]=="#"):
                            lowest_slot=ym
                            found=True
                            break
                        if(m[ym][x]=="O"):
                            m[lowest_slot][x]="O"
                            m[ym][x]="."
                            moved=True
                            lowest_slot+=1
                            found=True
                            break
                    if not found:
                        break

def rot90(m):
    return [list(l) for l in map("".join, zip(*reversed(m)))]

def main():
    inp_list = read()

    m=[list(r) for r in inp_list]
    pp(m)

    ys=len(m)
    xs=len(m[0])

#    roll(m)

    #m # north
    for i in range(1000000000):
        if(i%1==0):
            print(i, end=" ")
            res=0
            for x in range(xs):
                for y in range(ys):
                    if m[y][x]=="O":
                        res+=ys-y

            print(res)

        roll(m)
        m90=rot90(m) # west
        roll(m90)
        m180=rot90(m90) # south
        roll(m180)
        m270=rot90(m180) #east
        roll(m270)
        m=rot90(m270)

    res=0
    for x in range(xs):
        for y in range(ys):
            if m[y][x]=="O":
                res+=ys-y

    print(res)

def final():
    l=[64,65,63,68,69,69,65]

    start=71938

    index = (1000000000-71938) % 7
    print(l[index])


def final2():
    l=[96105, 96094, 96097, 96095, 96093, 96096, 96112, 96132, 96141, 96141, 96124]
    start=846
    index=(1000000000-846) % len(l)
    print(l[index])


if __name__ =="__main__":
    final2()
    #main()

