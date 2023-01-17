l=int(input("Enter the number of elements you want to enter in Array: "))
A=[]
for x in range(l):
   print("Enter the element number",x+1)
   num=int(input())
   A.append(num)
   
for x in range(l):
    min=x
    for y in range(x+1,l):
        if A[min]>A[y]:
            min=y
    A[x],A[min]=A[min],A[x]
print(A)
    