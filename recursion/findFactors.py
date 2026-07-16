# find divisors
from math import sqrt
n = 20
 
ans=[]

for i in range(1,int(sqrt(n))+1):
    
  if n%i == 0:
    ans.append(i)

    if n // i != i: 
      ans.append(n//i)
print(ans)










# for i in range(1,n//2):
#     if (n%i)==0:
#       ans.append(i)
#     else:
#        continue

# print(ans)  

