n=int(input("enter a number n : "))
a=0
b=1
print("fibonacci series")
print("0\n1")
for x in range(2,n):
c=a+b
print(c)
a=b
b=c
