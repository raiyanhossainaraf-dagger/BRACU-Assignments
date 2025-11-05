import sys
input= sys.stdin.readline

T=int(input())

MOD=10**9+7
answers=[]

for i in range(T):

    a11,a12,a21,a22=map(int,input().strip().split())
    x=int(input())

    A=[
            [a11,a12],
            [a21,a22]
                        ]
    

    def matrix_multipication(A,B):

        

        result=[
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
         
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
                                                    ]
        
        return result
    
    def matrix_power(A,power):

        res=[[1,0],[0,1]]

        while power>0:

            if power%2!=0:

                res=matrix_multipication(res,A)

            A=matrix_multipication(A,A)
            power=power//2

        return res
    

    answers.append(matrix_power(A,x))


for answer in answers:

    for row in answer:

        print(*row)
