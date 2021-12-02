arr = [1,85,65,67,8,6,4,5]
j = len(arr)
for i in range(0,int (len(arr)/2)):
    j = j-1
    arr[i],arr[j] = arr[j],arr[i]
print(arr)