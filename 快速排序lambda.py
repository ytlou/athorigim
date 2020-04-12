quick_sort = lambda array: array if len(array) <= 1 else quick_sort([
    item for item in array[1:] if item <= array[0]
]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

quick_sort([2,5,9,3,7,1,5])
#返回[1, 2, 3, 5, 5, 7, 9]
