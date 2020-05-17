n=int(input("enter the size of thevlist :"))
l=[]
for i in range(n):
le=int(input("enter the element :"))
l.append(le)
print(l)
x=0
k=int(input("enter the no. of smallest element to be searched,it should be less than the sixe of the list :"))
for i in range(n):
for j in range(n-1):
if l[j]>l[j+1]:
x=l[j]
l[j]=l[j+1]
l[j+1]=x
print("the value of smallest element in the list is :")
print(l[k-1])
