def order(l,n):
x=0
for i in range(n):
for j in range(n-1):
if l[j]>l[j+1]:
x=l[j]
l[j]=l[j+1]
l[j+1]=x
print(l)
print("the first element satisfying the condition is :",l[1]))
l=[]
for i in range(n):
l=[]
for i in range(n):
le=int(input("enter the element %d :"%(i+1)))
l.append(le)
print(l)
order(l,n)
