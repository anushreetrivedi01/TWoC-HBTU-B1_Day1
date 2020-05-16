def countX( tup, x ):
count = 0
for ele in tup:
if(ele == x):
count=count +1
return count
tup = (10,8,5,2,10,15,10,8,5,8,8,2)
enq = 4
enq1 = 10
enq2 = 8
print(Count(tup,enq),"times")
print(Count(tup,enq1),"times")
print(Count(tup,enq2),"times")
