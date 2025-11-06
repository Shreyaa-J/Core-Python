def isEvenOdd(n):
    return n%2==0

sr=int(input("Enter Starting Range : "))
er=int(input("Enter Ending Range : "))

if sr>er:
    print("Invalid Range")
else:
    for i in range(sr,er+1):
        flag=isEvenOdd(i)
        if flag:
            print(i,end=" ")    
