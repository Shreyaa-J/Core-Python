def isEvenOdd(n):
    return n%2==0

num=int(input("Enter number : "))
flag=isEvenOdd(num)

if flag:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")    