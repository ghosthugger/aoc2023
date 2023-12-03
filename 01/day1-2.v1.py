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
        first=v.index["1","2","3","4","5","6","7","8","9","0", "one", "two", "three", "four",
                     "five", "six", "seven", "eight", "nine"]

        rev_v=v[::-1]
        rev_v.index()
        last=v[::-1].index[n[::-1] for n in ["1","2","3","4","5","6","7","8","9","0", "one", "two", "three", "four",
                                             "five", "six", "seven", "eight", "nine"]]
            if c in ["1","2","3","4","5","6","7","8","9","0"] \
                    and last=="":
                last=c

        sum+=int(first)*10+int(last)

    print(sum)


if __name__ =="__main__":
    main()

