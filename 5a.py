import re

def isphonenumber(numstr):
    if len(numstr) !=12:
        return False
    for i in range(len(numstr)):
        if i==3 or i==7:
            if numstr[i] != '-':
                return False
            else:
                if numstr[i].isdigit():
                    return False
    return True

def reisphonenumber(numstr):
    phoneno=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if phoneno.match(numstr):
        return True
    else:
        return False

numstr=input("enter the phone number to be checked \n")
print("without regular expression")
if isphonenumber(numstr):
    print("It is a valid phone number")
else:
    print("not a phone number")
    
print("with regular expression")
if reisphonenumber(numstr):
    print("It is a valid phone number")
else:
    print("not a phone number")
    