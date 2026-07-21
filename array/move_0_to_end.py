#move 0 to end
# TC => O(n)
# SC => O(1)

def fun(arr):
    n = len(arr)

    #base case if the arr has only one element
    if len(arr) == 1:
        return 
    
    #find our 1st zero
    i = 0
    while i< n :
        if arr[i] == 0:
            break
        i+=1
    
    #base condition 2 if there's no zero 
    if i == n:
        return
    
    #main part
    j = i+1

    while j<n:
        if arr[j] != 0:
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
        j+=1
    return
    
    
a= [1,0,7]
fun(a)
print(a)