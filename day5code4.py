def knapsack(value,weight,capacity):
n = len(value) - 1
m = l[[-1]*(capacity +1) for _ in range(n+1)]
return knapsack_helper(value,weight,m,n,capacity)
def knapsack_helper(value,weight,m,i,w):
if[m][w] >= 0:
return m[i][w]
if i == 0:
q = 0
elif weight[i] <= w:
q= max(knapsack_helper(value,weight,m,i-1,w))
else:
q= knapsack_helper(value,weight,m,i-1,w)
m[i][w] = q
return q


n = int(input("enter the number of items: "))
value = input("enter the values of the {} item(s) in order:".format(n)).split()
value = [int(v) for v in value]
value.insert(0,none)
weight = [int(w) for w in weight]
weight.insert(0,none)
ans = knapsack(value,weight,capacity)
print("the maximum value of items that can be carried:",ans)
