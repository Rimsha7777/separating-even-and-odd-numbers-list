even=[]
odd=[]
k=input("enter your numbers seprated by comma = ")
k1=k.split(",")
for y in k1:
    
    if int(y)%2==0:
        even.append(y)
    else:
        odd.append(y)
print("even list is = ",even)
print("odd list is = ",odd)
