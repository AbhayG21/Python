# start=1
# stop=2
# cur_num=stop
# for row in range(1,5):
#     for col in range(start,stop):
#         cur_num-=1
#         print(cur_num,end="")
#     print("")
#     start=stop
#     stop+=row
#     cur_num=stop
    
    
# a=1
# n=4
# r=1
# x=0
# while(a<n):
#     r=x+a
#     x=r
#     while(r>a):
#         print(r-1,end="")
#         r-=1
#     print()
#     a+=1


# 1
# 3 2
# 6 5 4
# 10 9 8 7

a=1
start=2
end=1
r=1
n=5
while(r<=n):
    while(a>=end):
        print(a,end=" ")
        a-=1
    
    start=r+start
    a=a+start
    end=end+r
    print()
    r+=1