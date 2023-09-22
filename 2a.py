def f(N):
    if N<=0:
        print("Error! the entered number should be a positive")
        return 
    elif N==0:
        return[0]
    elif N==1:
        return[0,1]
    else:
        fn=[0,1]
        while len(fn)<N:
            fn_next=fn[-1]+fn[-2]
            fn.append(fn_next)
        return fn
    
N=int(input("Enter the number \n"))
result=f(N)
if result is not None:
    print("the result is ",result)