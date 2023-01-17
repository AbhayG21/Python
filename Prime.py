check=0
def func():
    global n
    n=int(input("Enter the number you want to be checked: "))
    if n<0:
        print("Enter a valid number to check!")
    elif n==0 or n==1:
        print("The number is neither prime nor composite")
    elif n==2:
        print(n,"is Prime")
    else:
        for x in range (2,n):
            if n%x==0:
                print(n,"is not a Prime Number")
                return
        return 1
check=func()
if check==1:
    print(n,"is Prime")
        