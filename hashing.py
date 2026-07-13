n = [1,2,3,3,2,1,4,5,6,4,2,5,7,4,6,10]
m =[3,54,65,3,6,2,6,7,2,10]

#with use of dictionary if given number of elemets are not fixed and spread around large range eg. 1 to 2000

freq_map = dict()

for num in n:
    if num in freq_map:
        freq_map[num] += 1
    else:
        freq_map[num]=1


for num in m:
    if num in freq_map:
        print(freq_map[num])
    else:
        print(0)


#with use of list if given list of items are fixed like 1 to 10.


# hash_list = [0]*11

# for num in n:
#     hash_list[num] += 1

# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])