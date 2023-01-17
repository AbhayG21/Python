n=int(input())
N=n+65
for x in range(N,65,-1):
    for s in range(x-1,65,-1):
        print(" ",end="")
    for y in range(N-x+1):
        print(chr(65),end="")
    print()
        