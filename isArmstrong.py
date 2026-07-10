n = 1634
num = n
nod = len(str(num))
ans = 0
while(num > 0):
    last_digit = num % 10
    ans += last_digit**nod
    num = num //10

if(ans == n):
    print(f'given number , {n} is an armstrong number')
else:
    print(f'given number , {n}is not an armstrong number')