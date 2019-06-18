def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    def binary_search_recursive_soln(array, target, lwr_bound, upr_bound):
        if lwr_bound > upr_bound:
            return -1
        
        mid = (lwr_bound + upr_bound) // 2
        
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            return binary_search_recursive_soln(array, target, lwr_bound, mid-1)
        else:
            return binary_search_recursive_soln(array, target, mid+1, upr_bound)
        
        
    
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

print(binary_search_recursive(array, target))
