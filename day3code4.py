def duplicate(List):
duplicateList=[]
for x in List:
if x is not in duplicateList:
duplicateList.append(x)
return duplicateList

Size = int(input("enter the number of elements you want to add in your list:"))
print("enter the elements in your list:")
List=[]
fpr x in range(Size):
List.append(input())
print("list after removing the duplicate element in the list is:",duplicate(List))
