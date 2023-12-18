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

    boxes=[[] for i in range(256)]
    res=0
    for i in inp_list[0]:

        label=None
        lens=None
        if '-' in i:
            label=i.split("-")[0]
        if '=' in i:
            label,lens=i.split('=')

        h=0
        for c in label:
            ascii=ord(c)
            h+=ascii
            h*=17
            h=h%256

        if lens==None:
            boxes[h]=[l for l in boxes[h] if l[0]!=label]
        if lens!=None:
            found=False
            for lensindex in range(len(boxes[h])):
                l,f =boxes[h][lensindex]
                if l==label:
                    found=True
                    boxes[h][lensindex]=(label,lens)
                    break

            if not found:
                boxes[h].append((label,lens))

            print(boxes)

        res+=h

    print(boxes)

    res=0
    for b in range(len(boxes)):
        for l in range(len(boxes[b])):
            t=(b+1)*(l+1)*int(boxes[b][l][1])
            print(t)
            res+=t

    print(res)

if __name__ =="__main__":
    main()

