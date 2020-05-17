def separate(1,n):
c=0
for i in range(n):
if l[i]==0:
c+=1
for i in range(c):
l[i]=0
for i in range(c,n):
l[i]=1
for i in range(n):
print(l[i],end=" ")


n=int(input("enter the size of the list :"))
l=[]
for i in range(n):
le=int(input("enter the list element.List element can only be 0 or 1:"))
l.append(le)
print(l)
print("List after sorting is:")
separate(l,n)
