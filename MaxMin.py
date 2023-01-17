l=int(input("Enter the number of elements you want to enter in Array: "))
A=[]
for x in range(l):
   print("Enter the element number",x+1)
   num=int(input())
   A.append(num)
max,min=A[0],A[0]
for y in range(l):
    if max<A[y]:
        max=A[y]
    if min>A[y]:
        min=A[y]
print(max,"is the largest out of array ",A)
print(min,"is the smallest out of array ",A)