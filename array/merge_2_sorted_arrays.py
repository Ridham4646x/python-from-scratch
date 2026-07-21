def fun(arr1,arr2):
    result = []

    for i in arr1:
        if i not in result:
            result.append(i)
    
    for j in arr2:
        if j not in result:
            result.append(j)
        
    return result

a = [1,1,1,2,4,5,7]
b = [1,2,3,6,7,8,9,10]

print(fun(a,b))