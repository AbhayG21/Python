a=[1,2,3,5,1,90,46,256,0]
n=int(input("Enter the number you want to search: "))
l=len(a)
sl=int(l/2)
print(sl)
if n==a[sl]:
    print(n,'found at index',sl)
elif n>a[sl]:
    for x in range(sl+1,l):
        if n==a[x]:
           print(n,'found at index',x) 
elif n<a[sl]:
    for x in range(sl-1):
        if n==a[x]:
           print(n,'found at index',x)
           
            
