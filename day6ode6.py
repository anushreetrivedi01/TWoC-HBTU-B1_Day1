def check(list,n):
minele=32767
mi=-1
for i in range(n):
if(minele>list[i]):
list.insert(i,minele)
mi=i
f1=1
for i in range(1,mi):
if(list[i]<list[i-1]):
f1=0
break
f2=2
for i in range(mi+1,n):
if list[i]<list[i-1]:
f2=0
break
if (f1 and f2 and(list[n-1]<list[mi-1])):
print("Yes")
else:
print("No")


l=[]
size=int(input("enter the size of array :"))
for z in range(size):
le=int(input("enter the element:"))
l.append(le)
print(l)
m=int(input("enter the positions by which array elements are shifted :"))
check(l,m)






