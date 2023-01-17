from sys import stdin

def insertionSort(arr, n) :  
    for x in range(1,n):
        current = arr[x]
        b = x-1
        while b >= 0 and current < arr[b]:
                arr[b + 1] = arr[b]
                b -= 1
        arr[b + 1] = current
    return arr
    #Your code goes here
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    insertionSort(arr, n)
    printList(arr, n)

    t-= 1