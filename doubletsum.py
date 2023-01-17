a=int(input("Enter the number of elements you want to enter in Array: "))
l=[]
for x in range(a):
   print("Enter the element number",x+1)
   num=int(input())
   l.append(num)
check=0
def func():
    global n
    n=int(input("Enter the number: "))
    for x in range(len(l)):
        a=l[x]
        for y in range(x+1,len(l)):
            b=l[y]
            if n==a+b:
                global check
                check=1
                print(n,"is the sum of",l[x],"at index",x,"and",l[y],"at index",y)
                return
func()
if check==0:
        print("No two numbers in python have the sum",n)