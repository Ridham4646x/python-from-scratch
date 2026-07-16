n = "abscdfabvhhdnvxsb"
m=['a','d' ,'s','p','v']

hash_list = [0]*26

#ascii code for a - z
#              97 - 122
for ch in n:
    ascii_code = ord(ch)
    index_num = ascii_code - 97
    hash_list[index_num] +=1

for ch in m:
    ascii_code = ord(ch)
    index_num = ascii_code -97
    print(hash_list[index_num])