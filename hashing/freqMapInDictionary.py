nums = [5,6,3,4,3,5,7,6,7,1,2,1,1,2,5,6,6,7,8,6,5,6,4]

freq_map = dict()

for i in range(0, len(nums)):

    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else :
        freq_map[nums[i]] =1 
print (freq_map)