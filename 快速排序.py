def quicksort(list):
  if len(list)<2:
    return array
  else:
    pivot=array[0]
    less = [i for i in array[1:] if i < =pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
 
