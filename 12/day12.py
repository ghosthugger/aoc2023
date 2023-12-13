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
        res.append((springs, groups))

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

def main():
    inp_list = read()
    #print(inp_list)
    assert(is_ok("#.#.###",[1,1,3])==True)
    assert(is_ok("##..###",[1,1,3])==False)
    assert(is_ok(".#...#....###.",[1,1,3])==True)


    res=0
    for springs, groups in inp_list:
        numq=springs.count("?")
        num_idx=[ind for ind, ch in enumerate(springs) if ch == '?']

        springs_list=list(springs)
        for n in range(2**numq):
            for b in range(numq):
                if (n & (1 << b) != 0):
                    springs_list[num_idx[b]]="#"
                else:
                    springs_list[num_idx[b]]="."

            springs_gen="".join(springs_list)

            if(is_ok(springs_gen, groups)==True):
                #print(springs_gen)
                res+=1

    print(res)


if __name__ =="__main__":
    main()

