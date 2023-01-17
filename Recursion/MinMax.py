n=int(input("Enter the number of elements you want to enter in Array: "))
A=[]
for x in range(n):
   print("Enter the element number",x+1)
   num=int(input())
   A.append(num)
def Minimum(A,n):
    if n==1:
        return A[0]
    return min(A[n-1],Minimum(A,n-1))
def Maximum(A,n):
    if n==1:
        return A[0]
    return max(A[n-1],Maximum(A,n-1))
print("Minimum: ",Minimum(A,n))
print("Maximum: ",Maximum(A,n))