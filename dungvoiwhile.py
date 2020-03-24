arr = [1,5,4,2,10,20,8]
n = len(arr)
i = 1
max = arr[0];
while i < n:
    if arr[i] > max:
        max = arr[i]
    i=i+1
print (max)
arr.remove(max)
i=1
newmax=arr[0]
n = len(arr)
while i < n:
    if arr[i] > newmax:
        newmax = arr[i]
    i=i+1
print(newmax)