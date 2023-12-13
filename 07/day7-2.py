from collections import Counter
from collections import defaultdict

def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        hand, bet = l.split(" ")
        res.append((hand.strip(),bet.strip()))

    #    assert(len(res)==1000)
    return res

def sort_hand(hand):
    c2v={'A':14,'K':13,'Q':12,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'J':1}
    #v2c={p[1]:p[0] for p in c2v.items()}

    sorted=[]
    for c in hand:
        sorted.append(c2v[c])
    #    sorted.sort(reverse=True)
    #    sorted=sort([c2v[c] for c in hands])
    tmp=[str(c).rjust(2,"0") for c in sorted]
    return "".join(tmp)


def joker_hand(hand):
    c2v={'A':14,'K':13,'Q':12,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    res=-1
    if(not 'J' in hand):
        return int(class_hand(hand))

    j_index = hand.find('J')
    for c,v in c2v.items():
        new_hand=hand[:j_index] + c + hand[j_index+1:]
        new_class=joker_hand(new_hand)
        res=max(res,new_class)

    return res

def class_hand(hand):
    sets=multiset([h for h in hand])

    res=-1
    if(len(sets)==1):
        res=7 # five of a kind
    elif(len(sets)==2):
        for i in sets:
            if(i[1]==4):
                res=6 # four of a kind
            if(i[1]==3):
                res=5 # full house
    elif(len(sets)==3):
        for i in sets:
            if(i[1]==3):
                res=4 # three of a kind
            if(i[1]==2):
                res=3 # two pair
    elif(len(sets)==4):
        res=2 #one pair
    elif(len(sets)==5):
        res=1 #high card

    if(res==-1):
        print(hand)

    assert(res!=-1)
    return str(res)

def typetoname(type):
    return ["none","high card", "one pair", "two pair", "three of a kind", "full house",
            "four of a "
            "kind",
            "five of a kind"][type]


def multiset(array):
    return set(Counter(array).items())

def main():
    inp_list = read()
    print(inp_list)

    print(sort_hand("KTJJT"))


    sorted_list=[]
    for hand, bet in inp_list:
        sorted_list.append((hand,bet,str(joker_hand(hand)),sort_hand(hand)))

    sorted_list.sort(key=lambda x:(x[2],x[3]), reverse=True)
    print(sorted_list)
    sorted_list.reverse()

    #    for hand, bet, c1, c2 in sorted_list:
    #        print(hand + " " + typetoname(int(class_hand(hand))))

    #    return


    rank=1
    wins=0
    for h,b,s1,s2 in sorted_list:
        print(rank)
        print(int(b))
        print(rank*int(b))
        print("")
        wins+=rank*int(b)
        rank+=1

    print(wins)
if __name__ =="__main__":
    main()

