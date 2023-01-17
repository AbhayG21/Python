n=int(input("Enter the number of elements you want to enter in Array: "))
A,B=[],[]
for x in range(n):
    print("Enter the element number",x+1)
    num=int(input())
    A.append(num)
    B.append(num)
A[0],A[n-1]=A[n-1],A[0]
print("Original list: ",B)
print("Swapped list: ",A)

