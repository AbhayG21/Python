a=int(input("Enter the number of elements you want to enter in Array: "))
l=[]

for x in range(a):
   print("Enter the element number",x+1)
   num=int(input())
   l.append(num)
#[1,2,3,4,5,6]
for x in range(len(l)):
    for y in range(len(l)-x-1):

        if l[y]>l[y+1]:
            l[y],l[y+1]=l[y+1],l[y]
print(l)
n=int(input("Enter the number: "))

def func(l):
    a,b=0,len(l)-1
    while(a!=b):
        sum=l[a]+l[b]
        if sum==n:
            global I1,I2
            I1,I2=a,b
            return 1
        elif sum>n:
            b=b-1
        else:
            a=a+1
z=func(l)
if z==1:
    print(n,"is the sum of",l[I1],"at position",I1+1,"and",l[I2],"at position",I2+1)
else:
    print("No two numbers in python have the sum",n)