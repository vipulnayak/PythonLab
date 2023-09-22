
# # 4. Write a program to find the sum of given two numbers using lambda function


a = int(input("Enter the first number:"))
b = int(input("Enter the second number"))
sum = lambda x,y:x+y
print("sum of given two numbers",sum(a,b))