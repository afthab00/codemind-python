n=int(input())
for i in range(n):
    c=list(map(int,input().split()))
    b=input()
    b=list(b)
    p=c[1]
    for i in range(1,c[1]):
        b=b[:p][::-1]+b[p:]
        p-=1
    m=''
    for i in b:
        m+=i
    print(m)