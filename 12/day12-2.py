import sys

def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        springs,groups_str=l.split(" ")
        groups=groups_str.split(",")
        groups=[int(g.strip()) for g in groups]
        res.append(((springs+"?")*4+springs, groups+groups+groups+groups+groups))
#        res.append(((springs+"?")*1+springs, groups+groups))
#        res.append((springs, groups))

    return res


def is_ok(springs, groups):
    splits=[s for s in springs.split(".") if(len(s))>0]

    res=True
    if(len(splits)==len(groups)):
        for g,s in zip(groups, splits):
            if g!=len(s):
                return False
    else:
        return False

    return res

cache = {}
count=0

def dfs(springs, groups):
    global cache
    global count
#    count+=1
#    print(springs,str(groups))
    if(springs,str(groups)) in cache:
        return cache[(springs,str(groups))]

    res=0
    if(len(springs)==0 and len(groups)==0):
        return 1

    if(len(springs)==0):
        return 0

    if(springs[0]=="."):
         for i in range(len(springs)):
             if(springs[i]!='.'):
                 break
         if(i==0):
             i=1

         return dfs(springs[i:], groups)

    if(len(groups)==0):
        if(springs.find('#') == -1):
#            cache[(springs,str(groups))] = 1
            return 1
        else:
#            cache[(springs,str(groups))] = 0
            return 0

    if(springs[0]=="#"  and groups[0]>1):
        i=1
        while(i<len(springs) and (springs[i]=="#" or springs[i]=="?") and i<groups[0]):
            i+=1
        springs="#"*i+springs[i:]

    if(len(springs)>=groups[0] and (springs[:groups[0]+1]=='#'*groups[0]+"."
                                    or springs[:groups[0]+1]=='#'*groups[0]+"?")):
        d=dfs(springs[groups[0]+1:], groups[1:])
        return d

    if(len(springs)>=groups[0] and springs=='#'*groups[0]):
        d=dfs(springs[groups[0]:], groups[1:])
        return d

#    if(not '?' in springs[:groups[0]]):
#        return 0

    if(springs[0]=='?'):
        d1=dfs('#'+springs[1:], groups)
        d2=dfs("."+springs[1:], groups)
        d=d1+d2
        cache[(springs,str(groups))] = d
        # if(d>0):
        #     print(d, end=' ')
        #     print(springs, end=' ')
        #     print(groups)
        #     print(d1, end=' ')
        #     print(springs[:i]+'#'+springs[i+1:])
        #     print(d2, end=' ')
        #     print(springs[:i]+'.'+springs[i+1:])
        #     print()
        res+=d

#    cache[(springs,str(groups))] = res
    return res

def dfs2(springs, groups):
    global cache

    if(springs,str(groups)) in cache:
        return cache[(springs,str(groups))]

    res=0
    if(len(springs)==0 and len(groups)==0):
        return 1

    if(len(springs)==0):
        return 0            #we still have groups left

    if(len(groups)==0):
        if(springs.find('#') == -1):
            return 1
        else:
            return 0

    if(springs[0]=="."):
        for i in range(len(springs)):
            if(springs[i]!='.'):
                break
        if(i==0):
            i=1

        return dfs2(springs[i:], groups)

    i=0
    bfirstq=True
    while i<=groups[0] and i<len(springs):
        if(springs[i]=="#"):
            if i<groups[0]:
                i+=1
            else:
                break
        elif(springs[i]=="."):
            if i<groups[0]:
                break
            else:
                i+=1
        elif(springs[i]=="?"):
            if(bfirstq==True):
                if(i!=groups[0]):
                    d=dfs2(springs[:i]+"."+springs[i+1:], groups)
                    cache[(springs[:i]+"."+springs[i+1:],str(groups))] = d
                    res+=d
                bfirstq=False
            i+=1

    if i==groups[0]+1 or (i==groups[0] and i==len(springs)):
        d=dfs2(springs[i:], groups[1:])
        cache[(springs[i:],str(groups[1:]))] = d
        res+=d

    return res

def main():
    sys.setrecursionlimit(20000)
    inp_list = read()
    #print(inp_list)
    global count
    global cache

    res=0
    assert(dfs2('?#?#?#?#?#?#?#?', [1,3,1,6]) == 1)
    assert(dfs2('?.###????.###', [1, 3, 1, 1, 3]) == 1)

    assert(dfs2("?", [1]) == 1)
    assert(dfs2("??", [1]) == 2)
    assert(dfs2("???", [1]) == 3)
    assert(dfs2("????", [1]) == 4)
    for springs, groups in inp_list:
#        count=0
        cache = {}
        l=dfs2(springs, groups)
        print(l)
        res+=l
#        print(count)

    print("res:", end=' ')
    print(res)


    "answer 17788038834111 is to low"
if __name__ =="__main__":
    main()

