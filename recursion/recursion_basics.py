# count = 0
# def rec_fun():
#     global count
#     if count==4 :
#         return
#     else:
        
#         print("that's recursion")
#         count+=1
#         rec_fun()

# rec_fun()        

def funWithParameter (str , n):
    
    # global count
    if n==0:
        return
    else:
        
        n-=1
        funWithParameter(str , n)
        print(n)
        
funWithParameter("hello",10)


