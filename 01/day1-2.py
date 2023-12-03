def read():
    with open('input.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            continue

        res.append(l.strip())

    return res

def argmin(lst):
    minidx=min(lst)
    for i in range(0,10):
        if(minidx==lst[i]):
            return i
    return 0

def main():
    inp_list = read()
    print(inp_list)

    sum=0
    for v in inp_list:
        first=""
        numbers=["one", "two", "three", "four",
                "five", "six", "seven", "eight", "nine"]
        rnumbers=["one"[::-1], "two"[::-1], "three"[::-1], "four"[::-1],
                 "five"[::-1], "six"[::-1], "seven"[::-1], "eight"[::-1], "nine"[::-1]]

        snumbers=["1", "2", "3", "4",
                 "5", "6", "7", "8", "9"]
        min_index = [v.index(s) if s in v else 1000 for s in numbers]

        v_repl=v
        if(min(min_index) < 1000):
            number_index=argmin(min_index)
            old_vrepl=v_repl
            v_repl=v_repl[:min(min_index)] + snumbers[number_index] + v_repl[
                                                                      min(min_index)+len(numbers[
                number_index]):]

        for c in v_repl:
            if c in ["1","2","3","4","5","6","7","8","9","0"] \
                    and first=="":
                first=c


        v_reverse=v[::-1]
        rmin_index = [v_reverse.index(s) if s in v_reverse else 1000 for s in rnumbers]

        rv_repl=v_reverse
        if(min(min_index) < 1000):
            number_index=argmin(rmin_index)
            old_rv_repl=rv_repl
            rv_repl=rv_repl[:min(rmin_index)] + snumbers[number_index] + rv_repl[
                                                                      min(rmin_index)+len(numbers[
                                                                                             number_index]):]


        last=""
        for c in rv_repl:
            if c in ["1","2","3","4","5","6","7","8","9","0"] \
                    and last=="":
                last=c

        print (int(first)*10+int(last))
        sum+=int(first)*10+int(last)

    print(sum)


if __name__ =="__main__":
    main()

