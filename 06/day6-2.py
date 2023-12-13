def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append(int(l.strip()))

    return res

def main():
    #    inp_list = read()

    #    print(inp_list)

    #Time:        47     98     66     98
    #Distance:   400   1213   1011   1540

    #Time:      7  15   30
    #Distance:  9  40  200
    # ((7,9),(15,40),(30,200)):

    res=[]
    for t,d in [(47986698,400121310111540)]:
        rres=[]
        for i in range(1,t+1):
            speed=i
            time=t-i
            distance=speed*time
            if(distance>d):
                rres.append(i)
        res.append(len(rres))

    print(res)
    t=1
    for n in res:
        t*=n
    print(t)
if __name__ =="__main__":
    main()

