"""
#
##
# #
#  #
#   #
######
"""
r=int(input("Rows: "))
for x in range(1,r+1):
    for y in range(1,x+1):
        if x<=2 or x==r:
            print("#",end="")
        elif y==1 or y==x:
            print("#",end="")
        else:
            print(" ",end="")
    print()    
        
            