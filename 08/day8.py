def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res={}

    instr=lines[0].strip()
    for l in lines[1:]:
        if(len(l.strip())==0):
            continue

        #FPF = (PTN, MPT)

        start,end=l.split("=")
        left,right=end.split(",")
        start=start.strip()
        left=left.strip("(").strip()[1:]
        right=right.strip(")").strip()[:3]

        res[start] = (left,right)

    return (instr, res)

def main():
    print(read())

    instr, guide=read()

    node="AAA"
    steps=0
    while(True):
        for c in instr:
            if(node=="ZZZ"):
                print(steps)
                return

            #print(node + " going " + c)
            if(c=="L"):
                node=guide[node][0]
            elif(c=="R"):
                node=guide[node][1]
            steps+=1

if __name__ =="__main__":
    main()