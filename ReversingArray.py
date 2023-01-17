l=int(input("Enter the number of elements you want to enter in Array: "))
A=[]
for x in range(l):
   print("Enter the element number",x+1)
   num=int(input())
   A.append(num)

A1=[]
for x in range(l-1,-1,-1):
    z=A.pop(x)
    A1.append(z)
print("The reversed Arrar is ",A1)
    
