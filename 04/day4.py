def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        index, wl=l.split(":")
        winners_str,loosers_str=wl.split("|")

        winners=winners_str.strip().replace("  ", " ").split(" ")
        loosers=loosers_str.strip().replace("  ", " ").split(" ")

        res.append((winners,loosers))

    return res

def main():
    inp_list = read()
    print(inp_list)

    print("\n")

    res=0
    for winners,loosers in inp_list:
        cardscore=0
        w = set(winners)
        for l in loosers:
            if l in w:
                if cardscore==0:
                    cardscore=1
                else:
                    cardscore*=2
        res+=cardscore

    print(res)

if __name__ =="__main__":
    main()
