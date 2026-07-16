def fun(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

a=[1,4,5,2,5,2,6,3,7]
print(fun(a))