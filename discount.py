a = int(input())
for i in range(a):
    #a,b,c,d = map(int,input() , split())
    x = int(input())
    y = int(input())
    z = int(input())
    s = int(input())
    if x-z<y-s :
        print("first")
    elif x-z>y-s: 
        print("second")
    else:
        print("Any")
