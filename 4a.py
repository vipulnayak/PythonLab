import random

def mergesort(lst):
    if len(lst)>1:
        mid=len(lst)//2
        lehalf=lst[:mid]
        rihalf=lst[mid:]
        
    mergesort(lehalf)
    mergesort(rihalf)
    
    i=j=k=0
    
    while i<len(lehalf) and j<len(rihalf):
        if lehalf[i] < rihalf[i]:
            lst[k]=lehalf[i]
            i+=1
        else:
            lst[k]=rihalf[j]
            j+=1
        k+=1
            
        while  i<len(lehalf):  
            lst[k]=lehalf[i]
            i+=1
            k+=1
        while j<len(rihalf):
            lst[k]=rihalf[j]
            j+=1
            k+=1
    return lst

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key>arr[i]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
   
# mergesort
     
mylist=[]

for i  in range(10):
    mylist.append(random.randint(0,999))

print("before sorting")
print(mylist)
print("after sorting")
mergesort(mylist)
print(mylist)

# insertion sort     
mylist=[]

for i  in range(10):
    mylist.append(random.randint(0,999))

print("before sorting")
print(mylist)
print("after sorting")
insertionsort(mylist)
print(mylist)
     