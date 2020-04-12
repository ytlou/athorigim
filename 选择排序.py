def findsmall(arr):
    small = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if small < arr[i]:
            small = arr[i]
            small_index = i
    return small_index

def sort(arr):
    newarr=[]
    for i in range(len(arr)):
        small=findsmall(arr)
        newarr.append(arr.pop(small))
    return newarr

print (sort([2,4,5,1,7]))
