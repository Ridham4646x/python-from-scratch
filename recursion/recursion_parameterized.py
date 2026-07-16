
def myFun(i,j,sum):
    if(i>j):
        print(sum)
        return
    else:
        sum += i
        myFun(i+1,j,sum)
          
    
myFun(1,10,0 )

def fun(n):
    if n==1:
        return 1
    else:
        return n+fun(n-1)

ans = fun(10)
print(ans)