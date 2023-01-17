"""
#####
#   #
#   #
#   #
#####
"""
r=int(input("Rows: "))
c=int(input("Columns: "))
for x in range(r):
    if x==0 or x==r-1:
        for y in range(c):
            print("#", end="")
    else:
        for y in range(c):
            if y==0 or y==c-1:
                print("#",end="")
            else:
                print(" ",end="")
    print()
    