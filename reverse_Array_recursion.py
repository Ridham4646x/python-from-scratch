a = [1,2,3,4,5,6,7,8,9]

def revArr(x,left,right):
    
    if  right<=left:
        return 
    
    else:
        x[left],x[right]=x[right],x[left]
        left+=1
        right-=1
        revArr(x,left,right)

revArr(a,0,len(a)-1)

print(a)