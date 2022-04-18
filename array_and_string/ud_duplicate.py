# Absolute value solution. 
# Use the array itself as hashtable. 
# The index of the array becomes the key and the -ve sign marks the element as visited.
# If -ve is encountered again it means the element was already visited.
arr = [1,2,3,2,1]
out = []
for i in range(0,len(arr)):
    if arr[abs(arr[i])] >= 0:
        arr[abs(arr[i])] = -arr[abs(arr[i])]
    else:
        out.append(abs(arr[i])) 
print("The repeated elements are :",out)
'''
arr = [1,2,3,1,5,1,2,3,4,5,6,4,32,2,1,22,2,31,4,325,325,435,45,4,5,45,45,45,4,5,5,4]
counter = {}
out=[]
for i in range(0,len(arr)):
    counter[arr[i]] = 0
for i in range(0,len(arr)):
    counter[arr[i]] = counter[arr[i]] + 1
for i in counter:
    if counter[i] > 1:
        out.append(i)
print("The repeated elements are : ",out)
'''

