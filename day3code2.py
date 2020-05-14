def permutation(List,String=""):
Set=set(List)
stringList=[]
if len(Set)==1:
String += "".join([String])
return list([String])
for x in Set:
List1=list(List)
S=String + x
list1.remove(x)
stringlist.extend(permutation(List1,s))
return stringlist

string=input("enter the string:")
List=permutation(list(string))
print("all the possible permutation for the given string is : " + ",".join(List))
