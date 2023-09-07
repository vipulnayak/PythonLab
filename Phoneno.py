import re

def isphonenumber(numStr):
    if len(numStr) !=12:
        return False
    for i in range(len(numStr)):
        if i==3 or i==7:
            if numStr[i] != "-":
                return False
        else:
            if numStr[i].isdigit() == False:
                return False
    return True

def reisphonenumber(numStr):
    phno_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if phno_pattern.match(numStr):
        return True 
    else:
        return False

ph_num=input("enter the Phone number")

print("Without using regular Expression")
if isphonenumber(ph_num):
    print("The Entered Number is a Valid Number")
else:
    print("The Entered Number is not a Valid Number")

print("with Using regular Expression")
if reisphonenumber(ph_num):
    print("The Entered Number is a Valid Number")
else:
    print("The Entered Number is not a Valid Number")
    
