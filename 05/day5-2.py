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
            seeds_i=[int(i) for i in numbers]

            for i in range(int(len(seeds_i)/2)):
                s=seeds_i[2*i]
                l=seeds_i[2*i+1]
                seeds.append((s,s+l-1))
            #print(seeds)
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


def childs3(inp):
    node,number=inp
    lir,hir=number #low input range, high input range
    node_ranges=[]
    for nfntrs in maps.items():
        nfnt,rs=nfntrs
        rs.sort(key=lambda tup: tup[1])
        nf,node_to=nfnt

        inp=0
        extra=[]
        for to,frm,length in rs:
            start=frm  #closed
            end=frm+length #open

            if inp<start:
                lfrm=inp
                lto=lfrm
                llength=start-inp
                extra.append((lto,lfrm,llength))

#            lfrm=start
#            lto=lfrm
#            extra.append((lto-frm+to,lfrm,length))
            inp=end
        extra.append((end,end,1000000000000))
        rs=rs.copy()
        rs.extend(extra)
        rs.sort(key=lambda tup: tup[1])
        if(nf==node):
            node_ranges.append((node_to,rs))

    res=[]
    for node_to,ranges in node_ranges:
        for to,frm,length in ranges:
            start=frm  #closed
            end=frm+length #open

            if(node_to=="temperature"):
                print("hej")

            if((start<lir and end<=lir) or (start>=hir and end>hir)): #1,5
                pass
            elif(start>=lir and end<hir): #3
                res.append((node_to,(start-frm+to,end-frm+to)))
            elif(start<lir and lir>start and end <= hir): #2
#                res.append((node_to,(start,start+lir-start)))
                res.append((node_to,(lir-frm+to,end-frm+to)))
            elif(hir>start and hir<end and start>lir): #4
                res.append((node_to,(start-frm+to,hir-frm+to)))
#                res.append((node_to,(hir,hir+end-hir)))
            elif(start<=lir and end>hir):
                res.append((node_to,(lir-frm+to,hir-frm+to)))

        for n,r in res:
            l,h=r
            if(not l<=h):
                print(res)
            assert(l<=h)

    return res



def childs2(inp):
    node,number=inp
    lir,hir=number #low input range, high input range
    node_ranges=[]
    for nfntrs in maps.items():
        nfnt,rs=nfntrs
        rs.sort(key=lambda tup: tup[1])
        nf,node_to=nfnt
        if(nf==node):
            node_ranges.append((node_to,rs))

    res=[]
    for node_to,ranges in node_ranges:
        for to,frm,length in ranges:
            lsrc=frm
            hsrc=frm+length-1

            if(lir>=hir):
                break

            left_in=lsrc<=hir and lsrc>=lir
            right_in=hsrc>=lir and hsrc<=hir

            if(lir<lsrc and hir<lsrc):
                res.append((node_to,(lir,hir)))
                lir=hir
            elif(lir>lsrc and lir>hsrc):
                pass
                #res.append((node_to,(lir,hir))) # TODO add logic for when to do this copy
                # TODO i.e is there a future intersecting interval lsrc,hsrc
            elif(lir<lsrc and hir<=hsrc and hir>lsrc):
                res.append((node_to,(lir,lsrc-1)))
                res.append((node_to,(lsrc-frm+to,hir-frm+to)))
                lir=hir
            elif(lir>=lsrc and lir<=hsrc and hir>hsrc):
                res.append((node_to,(lir-frm+to,hsrc-frm+to)))
                lir=hsrc+1
                # TODO what about hsrc+1 to hir? need to look at future intervals
            elif(left_in and right_in):
                res.append((node_to,(lir,lsrc-1)))
                res.append((node_to,(lsrc-frm+to,hsrc-frm+to)))
                lir=hsrc+1
                # TODO what about hsrc+1 to hir?
            elif(lir>lsrc and hir<hsrc):
                res.append((node_to,(lir-frm+to,hir-frm+to)))
                lir=hir

        if(lir<hir):
            res.append((node_to,(lir,hir)))

        for n,r in res:
            l,h=r
            if(not l<=h):
                print(res)
            assert(l<=h)

    return res

def childs(inp):
    node,number=inp
    lir,hir=number #low input range, high input range
    node_ranges=[]
    for nfntrs in maps.items():
        nfnt,rs=nfntrs
        nf,node_to=nfnt
        if(nf==node):
            node_ranges.append((node_to,rs))

    res=[]
    for node_to,ranges in node_ranges:
        found=False
        for to,frm,length in ranges:
            lsrc=frm
            hsrc=frm+length-1

            left_in=lsrc<=hir and lsrc>=lir
            right_in=hsrc>=lir and hsrc<=hir

            if(left_in and (not right_in)):
                res.append((node_to,(lsrc-frm+to,hir-frm+to)))
                if(((lsrc-1)-lir) >= 0):
                    res.append((node_to,(lir,lsrc-1)))
                found=True
            elif((not left_in) and right_in):
                res.append((node_to,(lir-frm+to,hsrc-frm+to)))
                if((lir-1-(lsrc)) >= 0):
                    res.append((node_to,(lsrc,lir-1)))
                found=True
            elif(left_in and right_in):
                res.append((node_to,(lsrc-frm+to,hsrc-frm+to)))
                if(((lsrc-1)-lir) >= 0):
                    res.append((node_to,(lir,lsrc-1)))
                if((hir-(hsrc+1)) >= 0):
                    res.append((node_to,(hsrc+1,hir)))
                found=True
            elif((lsrc<lir and hsrc<lir) or (lsrc>hir and hsrc>hir)):
                pass
#                res.append((node_to,(lir,hir)))
#                found=True
            elif((not left_in) and (not right_in)):
                res.append((node_to,(lir-frm+to,hir-frm+to)))
                found=True
        if(not found):
            res.append((node_to,(lir,hir)))

        for n,r in res:
            l,h=r
            if(not l<=h):
                print(res)
            assert(l<=h)

    return res


def main():
    global maps
    inp_list = read()
#    print(inp_list)
    seeds, maps=inp_list

    cs=[]
    for s in seeds:
        first_seed=("seed", s)
        cs.extend(childs3(first_seed))

    print(cs)
    #for c in cs:
    #    print(childs(c))

    minloc=0
    while(len(cs)>0):
#        print("cs:")
#        print(cs)
        el=cs.pop()
        print("el:")
        print(el)
        l,n=el
        if(l=="location"):
            if(minloc==0):
                l,h=n
                minloc=l
            else:
                l,h=n
                minloc=min(minloc,l)

            continue
        else:
            cs.extend(childs3(el))

        #print(cs)

    print("minloc")
    print(minloc)

if __name__ =="__main__":
    main()

