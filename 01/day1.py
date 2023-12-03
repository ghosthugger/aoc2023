def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append(l.strip())

    return res

def main():
    inp_list = read()
    print(inp_list)

    sum=0
    for v in inp_list:
        first=""
        for c in v:
            if c in ["1","2","3","4","5","6","7","8","9","0"]\
                    and first=="":
                first=c
        last=""
        for c in v[::-1]:
            if c in ["1","2","3","4","5","6","7","8","9","0"] \
                    and last=="":
                last=c

        sum+=int(first)*10+int(last)

    print(sum)


if __name__ =="__main__":
    main()

