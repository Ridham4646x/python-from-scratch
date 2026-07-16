def fun(a):
    for i in range(0,len(a)):
        min = i

        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
            else:
                continue
        a[min],a[i]=a[i],a[min]

    return a

a= [3,6,3,4,6,8,3,1,4]

ans = fun(a)
print(ans)