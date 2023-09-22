frst_test=int(input("Enter the marks of 1 test"))
sec_test=int(input("Enter the marks of 2 test"))
third_test=int(input("Enter the marks of 3 test"))

if(frst_test>sec_test):
    if(sec_test>third_test):
        total=frst_test+sec_test
    else:
        total=frst_test+third_test
else:
    if(frst_test>third_test):
        total=frst_test+sec_test
    else:
        total=sec_test+third_test

avg=total/2
print("the best avg marks is ",total)