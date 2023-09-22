# # 2. Write a program to enter a numberr and then calculate the sum of its digits




sumOfDigits = 0
num = int(input("Enter the number:"))
while(num!=0):
    temp = num % 10
    sumOfDigits = sumOfDigits + temp
    num = num // 10

print("The sum of digits is :",sumOfDigits)