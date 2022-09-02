m=int(input())
n=int(input())
s=0
k=0
for i in range(1,m):
    if m%i==0:
        s+=i
    if n%i==0:
        k+=i
if m==k and n==s:
    print('Amicable')
else:
    print('Not Amicable')