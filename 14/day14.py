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

def main():
    inp_list = read()

    m=[list(r) for r in inp_list]
    pp(m)

    ys=len(m)
    xs=len(m[0])

    for x in range(xs):
        moved=True
        while moved:
            pp(m)
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


    res=0
    for x in range(xs):
        for y in range(ys):
            if m[y][x]=="O":
                res+=ys-y

    print(res)



if __name__ =="__main__":
    main()

