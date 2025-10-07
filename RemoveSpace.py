str=input("Enter a String :")
i=0
newStr=""

strlen=len(str)-1

while(i<=strlen):
    if(str[i]!=" "):
        newStr=newStr+str[i]
    i=i+1
print("String after removing spaces :",newStr)        

# Sample Output : 
# Enter a String :Shree ji
# String after removing spaces : Shreeji