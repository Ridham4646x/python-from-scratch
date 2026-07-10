n = 1221
num = n

reversed = 0
i=4
while(i>0):
    last_digit = num%10
    reversed=(reversed*10)+last_digit 
    num= num//10
    i-=1
if(reversed == n):
    print(f'given number , {n} is a pelidrom number')
else:
    print(f'given number is not a pelidrom number')

