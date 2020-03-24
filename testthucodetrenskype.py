arr = [5,9,7,2,1,4]
i = 1
n = len(arr)
max1 = arr[0]
max2 = arr[0]
while i < n:
    if max1 < arr[i]:
        max2 = max1
        max1 = arr[i]
    elif max2 < arr[i]:
        max2 = arr[i]
    i=i+1
print(max2)
print(max1)