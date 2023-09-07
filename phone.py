import re
def isphonenumber(numStr):
    if len(numStr) != 12:
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
 phno_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
 if phno_pattern.match(numStr):
    return True
 else:
     return False
 
ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
 print("given phone number is Valid phone number")
else:
 print("given phone number is Invalid phone number")
 
print("Using Regular Expression")
if reisphonenumber(ph_num):
 print("given phone number is Valid phone number")
else:
 print("given phone number is Invalid phone number")
