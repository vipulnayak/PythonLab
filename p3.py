# # 3.write a program using for loop to calculate factorial of a number




num = int(input("Enter the number"))
if(num==0):
    fact =1
else:
    fact=1
    for i in range(1,num+1):
        fact = fact * i
print("Factorial of ",num, "is",fact)