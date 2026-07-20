# TC => O(2n)  ~ O(n)
# SC => O(n)

def fun(arr):
    freq_map = {}
    for i in range(0 , len(arr)):
       freq_map[arr[i]] = 0
    
    k = 0
    for j in freq_map:
        arr[k] = j 
        k+=1
     

    return j


a = [1,2,3,2,3,1,4,5,6,5,4,6,5,6,7,8,9,8,7,8,9,10]
print(fun(a))