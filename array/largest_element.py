def fun(arr):
    largest_ele = arr[0]
    for i in arr:
        if i>largest_ele:
            largest_ele = i
        else:
            continue
    return largest_ele

a = [3,54,6,230,-6,87,-3,90]

print(fun(a))