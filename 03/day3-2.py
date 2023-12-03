from collections import defaultdict

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
gears=defaultdict(lambda: [])

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


def get_gear(inp_list,x,y):
    global chars
    if(x<0 or x>=len(inp_list[0])):
        return False

    if(y<0 or y>=len(inp_list)):
        return False

    return inp_list[y][x] in "*"

def get_gears(i,x,y):
    pos=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    res=set()
    for dx,dy in pos:
        if(get_gear(i,x+dx,y+dy)):
            res.add((x+dx,y+dy))
    return res

def main():
    global chars
    global gears
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
    cur_gears=set()
    for y in range(len(inp_list)):
        for x in range(len(inp_list[y])):
            if inp_list[y][x].isnumeric():
                state=1
                current_number+=inp_list[y][x]
                if(surrounded_by(inp_list,x,y)):
                    surrounded=True
                cur_gears=cur_gears.union(get_gears(inp_list,x,y))
            elif state==1:
                number=int(current_number)
                if(surrounded):
                    res+=number
                    print(number)
                for g in cur_gears:
                    gears[g].append(number)
                state=0
                current_number=""
                surrounded=False
                cur_gears=set()

        if(state==1):
            number=int(current_number)
            if(surrounded):
                res+=number
                print(number)
            for g in cur_gears:
                gears[g].append(number)
            state=0
            current_number=""
            surrounded=False
            cur_gears=set()


    print(res)
    print(gears)

    resg=0
    for g, ns in gears.items():
        if(len(ns) ==2):
            resg+=ns[0]*ns[1]

    print(resg)


if __name__ =="__main__":
    main()

