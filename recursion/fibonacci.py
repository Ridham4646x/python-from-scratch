def fun(n):
    if n==1 or n==0:
        return n
    else:
        return fun(n-1)+fun(n-2)

print(fun(5))