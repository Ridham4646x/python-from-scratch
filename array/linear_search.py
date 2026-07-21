# TC => O(n)
# SC => O(1)

def fun(arr,key):
    for i in range(0,len(arr)):
        if arr[i] == key:
            return i+1
        else:
            continue

    return 'key not found'

a = [1,2,3,4,5,6,7,8,9]
print(fun(a,10))

