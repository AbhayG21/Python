"""
####
###
##
#
"""
r=int(input("Rows: "))
for x in range(r,0,-1):
    for y in range(x):
        print("#",end="")
    print()