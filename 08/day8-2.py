import math

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

    nodes=[c for c in guide.keys() if c[2]=="A"]
    start_nodes=["" for i in nodes]
    print(nodes)
    print("startnodes:")
    print(start_nodes)
    steps=0
    zpos=[-1 for i in nodes]
    clenght=[-1 for i in nodes]
    foundz=0
    num_nodes=len(nodes)
    while(True):
        #print("restart " + str(steps))
        #print(zpos)
        #print(clenght)
        for c in instr:
            #print(node + " going " + c)

            if(c=="L"):
                for n in range(len(nodes)):
                    nodes[n]=guide[nodes[n]][0]
            elif(c=="R"):
                for n in range(len(nodes)):
                    nodes[n]=guide[nodes[n]][1]
            steps+=1

#            endswithz=True
#            for n in nodes:
#                if(n[2]!="Z"):
#                    endswithz=False
#            if(endswithz):
#                print(steps)
#                return

            for n in range(len(nodes)):
                #print("matching startnode")
                #print(start_nodes[n])
                #print(nodes[n])
                if(nodes[n] == start_nodes[n]):
                    if(clenght[n]==-1):
                        clenght[n]=steps-zpos[n]
                        print(clenght)
                        foundz+=1

                if(foundz==num_nodes):
                    print("foundz " + str(steps))
                    print(zpos)
                    print(clenght)

                    return (steps, clenght)

                if(nodes[n][2]=="Z"):
                    if(zpos[n]==-1):
                        zpos[n]=steps
                        start_nodes[n]=nodes[n]




def main2(steps, c):
    #f=[14999, 20093, 17263, 16697, 12169, 20659]
    #c=[14999, 20093, 17263, 16697, 12169, 20659]
#    f=[2,3]
#    c=[2,3]
    step=0

    print("lcm")
    print(math.lcm(*c))
    print("gcd")
    print(math.gcd(*c))
    bigstep=math.lcm(*c)
    print(bigstep)
    start=[step for i in c]
    pos = start.copy()
    for i in range(len(c)):
        pos[i]=(pos[i]+bigstep)%c[i]
    step+=bigstep

    lenofc=len(c)
    while(pos.count(0)!=lenofc):
        if(pos.count(0)>3):
            for i in range(pos.count(0)):
                print("\t", end="")
            print(pos)
        #extra=1
#        for j in start:
#            if(j!=0):
#                extra*=j

        for i in range(len(c)):
            pos[i]=(pos[i]+bigstep)%c[i]
#            pos[i]=(pos[i]+(bigstep*extra))%c[i]

        step+=bigstep
#        for i in range(1):#len(c)):
#            if(pos[i] == 0):
#                if(start[i]==0):
#                    print("start")
#                    start[i]=f[i]
#                    print(start)
#                    print(step)


    print("journey is below steps")
    print(step)
    #A = [12, 24, 27, 30, 36]



if __name__ =="__main__":
    steps, c = main()
    main2(steps,c)
