def Sum(List,size,sum):
sumList = []
is Size==1:
for x in List:
sumList.append(sum + x)
return sumList
L=list(List)
for x in List:
L.remove(x)
sumList.extend(Sum(L,size-1,sum + x))
return sumList

def summation(List,size):
sumList = list(List)
for i in range(2,size+1):
sumList.extend(Sum(List,i,0))
number = 1
while True:
if number not in sumList:
print("the least integer which is not present in the list and also not be represented as the summation of sub elements is:",number)
break
number += 1

size=int(input("enter the no. of elements that you want to enter in the list:"))
List[]
print("enter the elements in the list one by one:")
for i in range(size):
List.append(int(input()))
summation(List,size)
