def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    
    pivot = find_pivot(input_list, 0, len(input_list) - 1)
    last_num = input_list[-1]
    
    if pivot == -1:
        return binary_search (input_list, 0, len(input_list) - 1, number)
    
    if input_list[pivot] <= number <= last_num:
        return binary_search (input_list, pivot, len(input_list) - 1, number)
    else:
        return binary_search (input_list, 0, pivot-1, number)
    
def binary_search(array, lwr_bound, upr_bound, target):
    if lwr_bound > upr_bound:
        return -1
    
    mid = (lwr_bound + upr_bound) // 2
    
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, lwr_bound, mid-1, target)
    else:
        return binary_search(array, mid+1, upr_bound, target)
    
    

def find_pivot(arr, low, high):
    '''
    finds the pivot index to then use in our binary search
    i.e. l = [6, 7, 8, 1, 2, 3] --> returns 3 (the index of 1)
    '''
    if low >= high:
        if arr[0] < arr[high]:
            return -1 #the list is not rotated
        return low
    
    mid = (low + high) // 2
    
    if (mid < high) and (arr[mid] > arr[mid + 1]): 
        return mid + 1
    if (mid > low) and (arr[mid] < arr[mid - 1]): 
        return mid 
    if arr[low] >= arr[mid]: 
        return find_pivot(arr, low, mid-1) 
    return find_pivot(arr, mid + 1, high) 
      
        
    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def tests():
    #find pivot tests
    assert(find_pivot([6, 7, 8, 1, 2, 3], 0, 5) == 3) #returns index of 3 which is the value 1
    assert(find_pivot([3], 0, 0) == 0)
    assert(find_pivot([2, 3, 6, 7, 8, 1], 0, 5) == 5)
    assert(find_pivot([8, 1, 2, 3, 6, 7], 0, 5) == 1)
    assert(find_pivot([1, 2, 3, 4, 5, 6], 0, 5) == -1) #not sorted!
    assert(find_pivot([6, 7], 0 , 1) == -1)
    
    #rotated array search tests
    assert(linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6) == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
    assert(linear_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1) == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
    assert(linear_search([6, 7, 8, 1, 2, 3, 4], 8) == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
    assert(linear_search([6, 7, 8, 1, 2, 3, 4], 10) == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))
    #edge cases
    assert(linear_search([6, 7, 8, 1, 2, 3, 4], 6) == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 6))
    assert(linear_search([6, 7, 8, 1, 2, 3, 4], 4) == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 4))
    assert(linear_search([6, 7], 6) == rotated_array_search([6, 7], 6))
    assert(linear_search([6, 7], 7) == rotated_array_search([6, 7], 7))
    assert(linear_search([1,2,3,4,5], 3) == rotated_array_search([1,2,3,4,5], 3))
    
    print('tests done')
    
tests()
