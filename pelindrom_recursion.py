def fun(x,left,right):
    if x[left]==x[right]:
        if right<=left:
            print('prlidrom')
        else:
            left+=1
            right-=1
            fun(x,left,right)
    else:
        print('not pelidrom')
a='nitinn'
fun(a,0,len(a)-1)

