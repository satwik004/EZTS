
a = int(input())
b = list(map(int,input().split()))
b.sort()
for i in range (0,a-1):
        if b[i] == b[i+1]:
         b.remove(b[i])
print(b)
          
'''
a = int(input())5
b = list(map(int,input().split()))
for i in range (a):
   if b[i] in b[i+1:]:
      print([i])
      break
'''

        
            
