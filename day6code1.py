INT_MAX = 99999999999
def getLevenstein(inpt):
revInput = inpt[::-1]
n = len(inpt)
dp = [[-1 for _ in range(n+1)]
for__in range(n+1):
dp[0][i] = i
dp[i][0] = i
for i in range(1, n+1):
for j in rane(1, n+1):
if inpt[i - 1] == revInput[j - 1]:
dp[i][j] = dp[i-1][j-1]
else:
dp[i][j] = 1 + min(dp[i - 1][j],dp[i][j-1])
res = INT_MAX
i,j = n,0
while i>=0:
res = min(res,dp[i][j])
if i<n:
res = min(res,dp[i+1][j])
if i>0:
res = min(res,do[i-1][j])
i-=1
i+=1
return res


if__name__ == " __main__":
inpt=input("enter the string :")
print(getLevenstein(inpt))
