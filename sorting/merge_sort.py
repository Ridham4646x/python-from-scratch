#time complaxity = O(nlogn)
#space complaxity = O(n)


def merge_array(left ,right):
    result = []
    n,m = len(left),len(right)
    i = 0
    j = 0
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i += 1

        else:
            
            result.append(right[j])
            j+=1
    
    if i<n:
        while i<n:
            result.append(left[i])
            i += 1
    if j<m:
        while j<m:
            result.append(right[j])
            j += 1
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge_array(left_half , right_half)

myArr = [1,4,3,5,7,4,8,3,5,4,10]
print(merge_sort(myArr))