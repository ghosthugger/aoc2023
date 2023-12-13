from collections import defaultdict
from enum import Enum

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

def char_at_pos(inp_list,x,y,charset):
    global chars
    if(x<0 or x>=len(inp_list[0])):
        return False

    if(y<0 or y>=len(inp_list)):
        return False

    return inp_list[y][x] in charset

def surrounded_by(i,x,y):
    pos=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    return any([char_at_pos(i,x+dx,y+dy,chars) for dx,dy in pos])

def get_gears(i,x,y):
    pos=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
    res=set()
    for dx,dy in pos:
        if(char_at_pos(i,x+dx,y+dy,set("*"))):
            res.add((x+dx,y+dy))
    return res

class ParseState(Enum):
    SEARCH=1
    PARSE=2

class State():
    def __init__(self):
        self.parse_state=ParseState.SEARCH
        self.current_number=""
        self.surrounded=False

    def reset(self):
        self.parse_state=ParseState.SEARCH
        self.current_number=""
        self.surrounded=False

    def parse(self, c):
        self.parse_state=ParseState.PARSE
        self.current_number+=c

def main():
    global chars
    global gears
    inp_list = read()
    print(inp_list)

    find_chars(inp_list)

    res=0
    state=State()
    cur_gears=set()
    for y in range(len(inp_list)):
        for x in range(len(inp_list[y])):
            if inp_list[y][x].isnumeric():
                state.parse(inp_list[y][x])
                if(surrounded_by(inp_list,x,y)):
                    state.surrounded=True
                cur_gears=cur_gears.union(get_gears(inp_list,x,y))
            elif state.parse_state==ParseState.PARSE:
                number=int(state.current_number)
                if(state.surrounded):
                    res+=number
                    print(number)
                for g in cur_gears:
                    gears[g].append(number)
                state.reset()
                cur_gears=set()

        if(state.parse_state==ParseState.PARSE):
            number=int(state.current_number)
            if(state.surrounded):
                res+=number
                print(number)
            for g in cur_gears:
                gears[g].append(number)
            state.reset()
            cur_gears=set()


    print(res)
    assert(res==540212)
    print(gears)

    resg=0
    for g, ns in gears.items():
        if(len(ns) ==2):
            resg+=ns[0]*ns[1]

    print(resg)
    assert(resg==87605697)


def find_chars(inp_list):
    global chars
    chars = set()
    for l in inp_list:
        for c in l:
            if not (c.isnumeric() or c == "."):
                chars.add(c)
    print(chars)


if __name__ =="__main__":
    main()

