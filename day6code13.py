l=[]
k=[]
n=int(input("enter the size of the list :"))
for i in range(n):
le=input("enter the list element :")
l.append(le)
print("string list is :",l)
for x in l:
e=float(x)
k.append(e)
print("the string list converted to float is :",k)
for i in range(n):
for j in range(i+1,n):
if (k[i]+k[j]+k[m]>1 and k[i]+k[j]+k[m]<2):
print("a=",k[i])
print("b=",k[j])
print("c=",k[m])
