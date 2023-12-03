def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        game, moves_str = l.split(":")
        moves = moves_str.split(";")
        game_lst=[]
        for m in moves:
            red=0
            green=0
            blue=0
            cubes_str = m.split(",")
            for c in cubes_str:
                if "green" in c:
                    green=int(c.strip().split(" ")[0])
                if "red" in c:
                    moped=c.split(" ")
                    red=int(c.strip().split(" ")[0])
                if "blue" in c:
                    blue=int(c.strip().split(" ")[0])
            game_lst.append((red,green,blue))

        res.append(game_lst)

    return res

def possible(game):
    res=True
    for (r,g,b) in game:
        if(r>12):
            res=False
        if(g>13):
            res=False
        if(b>14):
            res=False
    return res

def main():
    inp_list = read()
    print(inp_list)

    res=0
    for i in range(len(inp_list)):
        if possible(inp_list[i]):
            res+=i+1

    print(res)

if __name__ =="__main__":
    main()

