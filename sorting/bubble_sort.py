def fun(a):
    n = len(a)
    is_swap = False
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                is_swap = True
        if is_swap == False:
            return a   
    return a

a= [1,2,3,4,5,6]

print(fun(a))
