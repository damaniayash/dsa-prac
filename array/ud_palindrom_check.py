def palindrom():
    arr = "madamas"
    j = len(arr)
    for i in range (0,int(j/2)):
        j = j-1
        if arr[i] != arr[j]: output = False
        else: output = True
    return output
print(palindrom())