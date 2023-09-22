class Palistr:
    def __init__(self):
        self.isPali=False
    def chkPalindrome(self,mystr):
        if mystr == mystr[::-1]:
            return True
        else:
            return False

class Palint(Palistr):
    def __init__(self):
        self.isPali=False
    def chkPalindrome(self,val):
        temp=val
        rev=0
        while temp !=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10
        if val==rev:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali

str=input("enter the string\n")
stObj=Palistr()
if stObj.chkPalindrome(str):
    print("given string is a Palindrome \n")
else:
    print("Given string is not a palindrome\n")

val=int(input("enter a integer\n"))
valObj=Palint()
if valObj.chkPalindrome(val):
    print("given string is a Palindrome\n")
else:
    print("Given string is not a palindrome\n")
