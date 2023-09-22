n=int(input("Enter the number \n"))
num=str(n)
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("the number entered is a palindrome")
else:
    print("the number entered is not palindrome")
    
for i in range(10):
    if num.count(str(i)) > 0:
        print(str(i),"appears",num.count(str(i)),"time")