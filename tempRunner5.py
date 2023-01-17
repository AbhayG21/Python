## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=0
for x in range(0,n+1):
    if(x*x<=n):
        i=x
print(i)