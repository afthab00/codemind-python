n = int(input())
t = n
rev = 0
while n > 0: # 0 > 0
    r = n % 10 # r = 1%10 = 1
    rev = rev * 10 + r # rev = 4321
    n = n // 10 # n = 0
if t == rev:
    print("True")
else:
    print('False')
