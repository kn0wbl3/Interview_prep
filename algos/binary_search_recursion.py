def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    upper_bound = len(array) - 1
    lower_bound = 0
    #mid = (upper_bound + lower_bound) // 2
    
    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            lower_bound = mid
        else:
            upper_bound = mid
    
    return -1

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

print(binary_search(array, target))