
# # 1. write a python program to calculate roots of a quadratic equation

a = int(input("enter the values of a :"))
b = int(input("enter the values of b :"))
c = int(input("enter the values of c :"))
d = (b*b)-(4*a*c)
deno = 2*a
if(d>0):
    print("Real Roots")
    root1 = (-b + d**0.5)/deno
    root2 = (-b - d**0.5)/deno
    print("Root1 =",root1,"\tRoot2 =",root2)
elif(d==0):
    print("Eual Roots")
    root = -b/deno
    print("Root1 and Root2 =",root)
else:
    print("Imaginary Roots")