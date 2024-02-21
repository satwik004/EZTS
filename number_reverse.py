num = int(input())
reversed = 0
num = abs(num)
while num != 0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10
print(reversed)