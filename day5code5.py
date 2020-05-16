def two_way_sort(arr,arr_len):
l,r=0, arr_len - 1
k = 0
while(l<r):
while(arr[1] % 2 ! = 0):
l += 1
k += 1
while(arr[r] %2 == 0 and l<r):
r -= 1
if(l<r):
arr[1], arr[r] = arr[r],arr[1]
odd = arr[:k]
even = arr[k:]
odd.sort(reverse = True)
even.sort()
odd.extend(even)
return odd
