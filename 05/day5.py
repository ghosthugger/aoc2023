def read():
    with open('input.txt') as f:
        lines = f.readlines()

    seeds=[]
    mode=0
    ranges=[]
    res={}
    mfrom,mto="",""
    for l in lines:
        if(len(l.strip())==0):
            continue

        sl=l.strip()
        if( "seeds:" in l):
            text, numbers_str = sl.split(":")
            numbers=numbers_str.strip().replace("  ", " ").split(" ")
            seeds=[int(i) for i in numbers]
            continue

        if("to-soil" in sl):
            mfrom,mto = sl.split("-to-")
            mto=mto.strip(" map:")
            ranges=[]
            continue

        if( "-to-" in l):
            res[(mfrom,mto)]=ranges
            ranges=[]
            mfrom,mto = sl.split("-to-")
            mto=mto.strip(" map:")
            continue

        #print(sl)
        f,t,l=sl.split(" ")
        ranges.append((int(f),int(t),int(l)))

    res[(mfrom,mto)]=ranges
    return [seeds,res]

maps={}

def childs_i(node, numbers):
    node_ranges=[]
    for nfntrs in maps.items():
        nfnt,rs=nfntrs
        nf,nt=nfnt
        if(nf==node):
            node_ranges.append((nt,rs))

    res=[]
    for n in numbers:
        for nt,rs in node_ranges:
            found=False
            for t,f,l in rs:
                if n>=f and n<f+l:
                    res.append((nt,n-f+t))
                    found=True
            if(not found):
                res.append((nt,n))
    return res

def childs(inp):
    node,number=inp
    node_ranges=[]
    for nfntrs in maps.items():
        nfnt,rs=nfntrs
        nf,nt=nfnt
        if(nf==node):
            node_ranges.append((nt,rs))

    res=[]
    for nt,rs in node_ranges:
        found=False
        for t,f,l in rs:
            if number>=f and number<f+l:
                res.append((nt,number-f+t))
                found=True
        if(not found):
            res.append((nt,number))
    return res




def main():
    global maps
    inp_list = read()
    #print(inp_list)
    seeds, maps=inp_list

    cs = childs_i("seed", seeds)
    #print(cs)
    #for c in cs:
    #    print(childs(c))

    minloc=0
    while(len(cs)>0):
        el=cs.pop()
        l,n=el
        if(l=="location"):
            if(minloc==0):
                minloc=n
            else:
                minloc=min(minloc,n)

            # print ((l,n))
            continue
        else:
            cs.extend(childs(el))

        #print(cs)

    print(minloc)

if __name__ =="__main__":
    main()

