
arr = [10, 324, 45, 90, -2, 6, 9, 99]
max = arr[0]
for i in range (1, len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)
arr.remove(max)
newmax = arr[0]
for i in range (1, len(arr)):
    if arr[i] > newmax:
        newmax = arr[i]
print(newmax)

