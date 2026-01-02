import sys
import bisect

def main():

    input = sys.stdin.readline

    t = int(input())
    out = []

    for _ in range(t):

        n,m= map(int, input().split())
        tasks =[]

        for _ in range(n):
            s,e= map(int, input().split())
            tasks.append((e, s))  

        tasks.sort()

        people = []  
        count = 0

        for e,s in tasks:
           

            idx=bisect.bisect_left(people, s)

            if idx > 0:

                
                people.pop(idx - 1)
                bisect.insort(people, e)
                count += 1

            elif len(people)<m:

                
                bisect.insort(people, e)
                count += 1
           

        out.append(str(count))

    sys.stdout.write("\n".join(out))



if __name__ == "__main__":
    main()
