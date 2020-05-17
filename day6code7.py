def A(a,b):
if a==0:
return b+1
elif (a>0 and b==0):
return A(a-1,1)
elif (a>0 and b>0):
returnA(a-1,A(a,b-1))




m=int(input("enter a non negative integer :"))
n=int(input("enter a non negative integer ;"))
print(A(m,n))
