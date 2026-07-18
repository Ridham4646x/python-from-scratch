def fun(arr):
    largest = arr[0]
    second_largest = arr[0]

    for i in arr:
        if i<largest and i>second_largest:
            second_largest = i
        elif i>largest:
            second_largest = largest
            largest = i
        else:
            continue
    
    return second_largest


a = [55 , 32,32,97 , -55 , 45 ,32,88 ,21,97]

print(fun(a))