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
    inp_list = read()
    print(inp_list)


if __name__ =="__main__":
    main()

