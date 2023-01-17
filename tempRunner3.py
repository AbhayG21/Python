P=int(input("Enter initial amount: "))
# R=float(input("Enter rate: "))
R=35
T=int(input("Enter months: "))
final=0
for x in range(T):
    intr=P*R/100
    P=P+intr
    print(P,"ends month",x+1,"...")
    print()
    if (P>=8000 and P<=15000):
        R=50
    elif(P>15000):
        R=65
