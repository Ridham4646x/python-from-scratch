def my_fun(arr):
    n = len(arr)

    arr.sort()

    for i in range(0,n):
        if arr[i+1] != i+1:
            return i+1
        else:
            continue

def optimal_fun(arr):
    n=len(arr)

    return n*(n+1)/2 - sum(arr)


a = [9,6,4,2,3,5,7,0,1]
print(my_fun(a))
print(optimal_fun(a))

