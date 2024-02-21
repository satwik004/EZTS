a = int(input())
b = int(input())
c = int(input())
if a<b<c:
    c = 0
elif c<a<b:
    b = 0
else:
    a = 0
if a<b and b>c:
    print(b)
elif c<a and a>b:
    print(a)
else:
    print(c)
 
