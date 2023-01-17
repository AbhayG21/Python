from tkinter import N


# a=float(input("Enter the Quantity: "))
a=3.5
n=int(input("Enter the Months:"))
for x in range(0,n):
    # print("Enter the Quantity addition in month",x+1,": ",end="")
    # z=float(input())
    z=0.2
    a=(a+z)+((a+z)*0.04825)
print(a)
print(0.2*n)
