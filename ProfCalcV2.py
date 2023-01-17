import time
P=int(input("Enter the initial amount: "))
R1=55
R2=35
T=int(input("Enter months: "))

for x in range(1,T+1):
    intr=P*R2/100
    P=P+intr
    
    P2=(P/2)-79
    P=P/2
    intr2=P2*R1/200
    P2=intr2+P2
    print()
    P2=P2-(0.03*P2)
    P+=P2
    print(P,"ends month",x,"...")
    if (P>=8000 and P<=15000):
        R2=50
    elif(P>15000):
        R2=65