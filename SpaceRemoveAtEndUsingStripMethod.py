# Strip() - method is used to remove any leading (spaces at the beginning) 
# and trailing (spaces at the end) 
# characters (space is the default leading character to remove)

# There are 2 types of strip() methods:
# 1)lstrip() - removes spaces from the left side of the string
# 2)rstrip() - removes spaces from the right side of the string

# Example
str=input("Enter a String : ")
print("Original String :",str)
str2=str.lstrip()
print("After Removing Spaces from left :",str2)
#Output: 
# Enter a String :                         hii hii
# Original String :                         hii hii
# After Removing Spaces from left : hii hii