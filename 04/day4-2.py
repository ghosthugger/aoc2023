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

    cardscores=[]
    i=1
    for winners,loosers in inp_list:
        cardscore=0
        w = set(winners)
        for l in loosers:
            if l in w:
                if cardscore==0:
                    cardscore=1
                else:
                    cardscore+=1

        cardscores.append((i,cardscore))
        i+=1

    cardcount=[1 for c in cardscores]


    for pos, score in cardscores:
        i=pos-1
        count=cardcount[i]

        for copies in range(count):
            for j in range(pos,min(pos+score, len(cardscores))):
                cardcount[j]+=1


    print(cardcount)
    res=sum(cardcount)
    print(res)

if __name__ =="__main__":
    main()
