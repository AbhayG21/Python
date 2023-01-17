n=int(input())
l=n
print()
for x in range(n):
    for y in range(n+1):
        if x==n-2 and y==1:
            print(" ",end="")
        elif x==n-2 and y==2:
            print(" ",end="")
        elif x==n-2 and y==n-1:
            print("|",end="")
        elif x==n-1 and y==n-1:
            print("|",end="")
        elif x==n-1 or x==n-2 or x==n-3:
            print("#",end="")
        else:
            print(" ",end="")
    for z in range(2):
        if x==n-1:
            print("#",end="")
        else:
            print(" ",end="")
        
    for a in range(x+1):
        print("#",end="")
    for s1 in range(n-x-1):
        print("  "*2,end="")
    for b in range(x+1,0,-1):
        print("#",end="")
    print()
for x in range(n):
    for y in range(n+1):
        if x==1 and y==1:
            print(" ",end="")
        elif x==1 and y==2:
            print(" ",end="")
        elif x==0 and y==n-1:
            print("|",end="")
        elif x==1 and y==n-1:
            print("|",end="")
        elif x==0 or x==1 or x==2:
            print("#",end="")
        else:
            print(" ",end="")
    for z in range(2):
        if x==0:
            print("#",end="")
        else:
            print(" ",end="")
    for a in range(l):
        print("#",end="")
    for s1 in range(n-l):
        print("  "*2,end="")
    for b in range(l,0,-1):
        print("#",end="")
    l-=1
    print()
