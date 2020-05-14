size1 =int(input("enter the number of elements that you want to enter in List1:"))
List1=[]
print("enter the elements in list 1 one by one:")
for i in range(sixe1):
List1.append(input())
size2= int(input("enter the no. of elements that you want to enter in list2:"))
List2=[]
print("enter elements in list 2 one by one")
for i in range(size2):
List2.append(input())
intersectionList=list(set(List1).intersection(set(List2)))
print("the intersection of List1 and List2 is:"'intersectionList)
