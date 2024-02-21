num = int(input())
reversed= 0
num = num * -1
while num != 0:
    digit = num % 10
    reversed= reversed * 10 + digit
    num //= 10
print(reversed * -1)