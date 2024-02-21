a = int(input())
for i in range (a):
    x,y = map(int,input().split())
    z = x*y
    b = 0
    if(z%4 == 0):
        print(z//4)
    else:
        print((z//4)+1)
#using while loop
#while b>0:
#  z -= 4
#  b +=1