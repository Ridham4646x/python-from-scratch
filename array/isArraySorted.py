def fun(arr):
    for i in range(0,len(arr)-1):
        if arr[i]<=arr[i+1]:
            continue
        else:
            return False
    return True

a = [1,2,3,4,5,2,7,7,9]

print(fun(a))
