a = int(input())
for i in range (a):
    a,b = map(int,input().split())
    if a<=b:
        print("0")
    else:
        c = a-b
        if c%4 == 0:
            print(c//4)
        else:
            print((c//4)+1)
    