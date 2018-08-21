import copy
#Reverse the whole list using list methods.
a=[1,2,3,4,5,6]
a.reverse()
print(a)

#Print all the uppercase letters from a string.
a=input("Enter Any string")
c=a.upper()
print(c)

#Split the user input on comma's and store the values in a list as integers.

lst=[]
a=0
strr=input("enter number")
str1=strr.split(',')
for i in range(0,len(str1)):
    a=int(str1[i])
    lst.append(a)
print("list",lst)

#Check whether a string is palindromic or not.
str1=input("Enter String")
str2=str1[::-1]
if str1==str2:
    print("string is pallindromic")
else:
    print("string is not pallindromic")
  
    
#Make a deepcopy of a list and write the difference between shallow copy and deep copy.

lst=[1,2,[3,4],5]
lst1=copy.deepcopy(lst)
lst1[2][1]= 7
print(lst)
print(lst1)
