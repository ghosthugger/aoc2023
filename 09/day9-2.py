def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append([int(i.strip()) for i in l.split(" ") ])

    return res

def diffs(s):
    res=[]

    last_s=s
    res.append(s)
    while(last_s.count(0)!=len(last_s)):
        next_s=[]
        for i in range(len(last_s)-1):
            next_s.append(last_s[i+1]-last_s[i])
        res.append(next_s)
        last_s=next_s

    return res

def main():
    res = read()


    extrapol=[]
    all_diffs=[diffs(s) for s in res]
    for dso in all_diffs:
        ds=dso.copy()
        print("new sequence")
        for l in ds:
            print(l)

        fill=None
        fills=[]

        ds.reverse()
        for sso in ds:
            ss=sso.copy()
            ss.reverse()
            if(fill==None):
                fill=0
                fills.append(fill)
            else:
                n = ss[-1]-fill
                fills.append(n)
                fill=n

        print(fills)
        extrapol.append(fills[-1])

    print("extrapool")
    print(extrapol)
    print(sum(extrapol))

if __name__ =="__main__":
    main()

