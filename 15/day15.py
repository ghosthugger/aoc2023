def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        parts=l.split(",")
        res.append([p.strip() for p in parts])

    return res

def main():
    inp_list = read()
    print(inp_list)

    res=0
    for i in inp_list[0]:
        h=0
        for c in i:
            ascii=ord(c)
            h+=ascii
            h*=17
            h=h%256
        res+=h

    print(res)

if __name__ =="__main__":
    main()

