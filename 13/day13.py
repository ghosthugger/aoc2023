def read():

    patterns=[]
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            patterns.append(res)
            res=[]
            continue


        res.append(l.strip())

    return patterns

def pp(p):
    for l in p:
        print(l)

    print()

def reflections(pattern):
    ys=len(pattern)
    xs=len(pattern[0])
    res=[]
    for x in range(1,xs):
        mirror=True
        for y in range(ys):
            w=min(xs-x, x)
            leftp=pattern[y][x-w:x]
            rightp=pattern[y][x:x+w]
            leftp=leftp[::-1]
            if leftp!=rightp:
                mirror=False

        if mirror:
            res.append(x)

    return res

def main():
    inp_list = read()

    res=0
    for pattern in inp_list:
        pp(pattern)
        refl=reflections(pattern)
        print(refl)
        pl=[list(r) for r in pattern]
        pattern90=[l for l in map("".join, zip(*reversed(pl)))]
        print("90 deg")
        print("\n".join(map("".join, zip(*reversed(pattern)))))
        refl90=reflections(pattern90)
        if(len(refl90)>0):
            xs90=len(pattern90[0])
            refl90=[xs90-i for i in refl90]
        print(refl90)

        if(len(refl)==1):
            res+=refl[0]
        if(len(refl90)==1):
            res+=refl90[0]*100


    print(res)



if __name__ =="__main__":
    main()

