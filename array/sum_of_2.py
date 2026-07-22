def fun(arr,target):
    n = len(arr)

    for i in range(0 , n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return i,j
            else:
                continue


a = [5,9,1,2,4,15,6,3]

print(fun(a,13))