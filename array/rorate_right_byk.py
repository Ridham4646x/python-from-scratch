#rotate right by one
# # TC => O(n-1)   ~~ O(n)
# # SC => O(1)

# def fun(arr,k):
#     n = len(arr)

#     temp = arr[n-1]
#     while k>0:
#         for i in range(n-2,-1,-1):
#             arr[i+1] = arr[i]
#         arr[0] = temp
#         k -=1

#     return arr

# a = [1,2,3,4,5,6,7,8,9,10]
# print(fun(a,3))



#rotate right by k elements
#push-  pop
#brute force solution
# TC => O(r* n)
# SC => O(1)


# def fun (arr , k):
#     n = len(arr)
#     rotates = k%n

#     for _ in range(0,rotates):   #O(r)
#         e = arr.pop()            #O(1)
#         arr.insert(0,e)          #O(n)

# a = [1,2,3,4,5,6,7,8,9,10]

# fun(a,10)
# print(a)





# #better solution
# # TC => O(n)
# # SC => O(1)
# def fun (arr , k):
#     n = len(arr)
#     rotates = k%n

#     arr[:] = arr[n-k:] + arr[:n-k]

    

# a = [1,2,3,4,5,6,7,8,9,10]

# fun(a,5 )
# print(a)



#optimal  solution
# TC => O(n)
# SC => O(1)

def reverse (arr ,left , right,k):
    n = len(arr)
    while left<right:
        arr[left], arr[right] = arr[right] ,arr[left]
        left += 1
        right += 1

reverse(n-k,n-1)
reverse(0,n-k-1)
reverse(0,n-1)

a = [1,2,3,4,5,6,7,8,9,10]

reverse(a,0,len(a),5 )
print(a)