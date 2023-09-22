s=input("the sentence to be entered is\n")
w,d,u,l=0,0,0,0
l_w=s.split()
w=len(l_w)
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isupper():
        u=u+1
    elif c.islower:
        l=l+1

print("words =",w)
print("digit =",d)
print("upper =",u)
print("lower =",l)     