"""
    #
   ##
  ###
 ####
#####      
"""
r=int(input("Rows: "))
for x in range(1,r+1):
    n=x
    for y in range(r-n):
        print(" ",end="")
    for y in range(n):
        print("#",end="")
    print()    