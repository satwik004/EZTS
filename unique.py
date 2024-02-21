a = int(input())
b = list(map(int,input().split()))
c = []
for i in range(a):
    x = b.count(b[i])
    if(x == 1):
        c.append(b[i])
for k in c:
    print(k,end=" ")