#consicutive one's

#my solution
# TC => O(n^2)
# SC => O(1)
def my_fun(arr):
    n = len(arr)
    count = 0
    max_count = 0

    for i in range(0,n):
        if arr[i] == 1:
            for j in range(i,n):
                if arr[j] == 1:
                    count += 1
                else:
                    break
            if max_count < count:
                max_count = count
                count = 0
            else:
                count = 0
            i = j
    
    return max_count

#optimal solution
# TC => O(n)
# SC => O(1)

def fun(arr):
    n = len(arr)

    count = 0
    max_count = 0

    for i in range(0,n):
        if arr[i] == 1:
            count += 1
        else:
            max_count = max(max_count , count)
            count = 0
    
    return max(max_count,count)


a = [1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1]
print(my_fun(a))
print(fun(a))