from tkinter import N

# a=float(input("Enter the Quantity: "))
a=3.5
n=int(input("Enter the Years:"))
for x in range(0,n*12):
    # print("Enter the Quantity addition in month",x+1,": ",end="")
    # z=float(input())
    # z=0.2
    a=(a)+(a*0.04825)
    print("month",x+1,"->",a," ->",round(a*20*80))
# print(a)
# print(0.2*n)
