def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append(l.strip())

    return res

chars=set()

def non(inp_list,x,y):
    global chars
    if(x<0 or x>=len(inp_list[0])):
        return False

    if(y<0 or y>=len(inp_list)):
        return False

    return inp_list[y][x] in chars

def surrounded_by(i,x,y):
    return non(i, x-1, y-1) \
           or non(i, x, y-1) \
           or non(i, x+1,y-1) \
           or non(i, x+1,y) \
           or non(i, x+1, y+1) \
           or non(i, x, y+1) \
           or non(i, x-1,y+1) \
           or non(i, x-1,y)

def main():
    global chars
    inp_list = read()
    print(inp_list)

    print(non(inp_list,3,1))

    chars=set()
    for l in inp_list:
        for c in l:
            if not (c.isnumeric() or c=="."):
                chars.add(c)
    print(chars)
    res=0
    state=0
    current_number=""
    surrounded=False
    for y in range(len(inp_list)):
        for x in range(len(inp_list[y])):
            if inp_list[y][x].isnumeric():
                state=1
                current_number+=inp_list[y][x]
                if(surrounded_by(inp_list,x,y)):
                    surrounded=True
            elif state==1:
                number=int(current_number)
                if(surrounded):
                    res+=number
                    print(number)
                state=0
                current_number=""
                surrounded=False

        if(state==1):
            number=int(current_number)
            if(surrounded):
                res+=number
                print(number)
            state=0
            current_number=""
            surrounded=False


    print(res)

if __name__ =="__main__":
    main()

