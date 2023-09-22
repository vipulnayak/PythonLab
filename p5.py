# # 5. write a program to swap two numbers using fucntions




def swap(a,b):
    a,b = b,a
    print("After swaping :")
    print("First Number :",a)
    print("Second Number :", b)

a= int(input("Enter the first number:"))
b = int(input("Enter the Second number :"))
print("Before swaping:")
print("First Number :",a)
print("Second Number :", b)
swap(a,b)

