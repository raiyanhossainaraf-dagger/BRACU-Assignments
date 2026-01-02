import sys

def main():

    
    input = sys.stdin.readline

    n =int(input())
    tasks =[]

    for _ in range(n):

        
        s,e= map(int, input().split())
        tasks.append((e, s))  

    tasks.sort()

    res = []
    last_end = -1

    for e, s in tasks:


        if s > last_end:      

            res.append((s, e))
            last_end = e

    out = []
    out.append(str(len(res)))


    for s, e in res:

        out.append(f"{s} {e}")


    sys.stdout.write("\n".join(out))

if __name__=="__main__":

    main()
