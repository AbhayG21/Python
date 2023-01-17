P=float(input("Initial Value= "))
temp=P
m=int(input("Months= "))
r=float(input("Rate= "))
r=r/100
for x in range(1,(m*30)+1):
    
    
    s=P*r
    P=P+s
    if x%30==0:
        print("Month",x//30,":",P,"\n")
    if x%30==0 and x!=m*30:
        z=float(input("Enter the amount to be deposited: "))
        P=P+z
        temp=temp+z
print("Final Value= ",int(round(P,0)))

print("\n")
prof=((P-temp)/temp)*100
prof=int(round(prof,0))
print("Profit Percent=",str(prof)+"%")