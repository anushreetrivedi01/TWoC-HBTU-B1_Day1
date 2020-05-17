def sorting(a,b,n,m):
c=[]
k=m+n
i1=0
i2=0
i=0
while (i1<n and i2<m):
if (a[i1]<b[i2):
c.append(a[i1])
i1+=1
else:
c.append(b[i2])
i2+=1
i+=1
if i1==n:
while i2<m:
c.append(b[i2])
i2+=1
i+=1
elif i2==m:
while i1<n:
c.append(a[i1])
i1+=1
i+=1
for z in range(k):
print(c[z])


p=[]
q=[]
r=int(input("enter the size of list 1 :"))
for i in range(r):
pe=int(input("enter element %d :"%(i+1)))
p.append(pe)
s=int(input("enter the size of list 2 :"))
for i in range(s):
qe=int(input("enter the element%d :"%(i+1)))
q.append(qe)
print(p)
print(q)
print("the merged sorted list is :")
sorting(p,q,r,s)


