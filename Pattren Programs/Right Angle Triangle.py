n=int(input("Enter Num :"))

for i in range(1,(n+1)):
      #explicit spaces
      for k in range(n,i,-1):
        print(" ",end="")
      #to print stars
      for j in range(1,(i+1)):
        print("*",end="")
      print()
