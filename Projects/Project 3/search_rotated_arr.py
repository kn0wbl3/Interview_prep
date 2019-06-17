# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:43:42 2019

@author: amanuele2
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    first_num = input_list[0]
   
    st_indx = 0
    end_indx = len(input_list) - 1
   
    while st_indx < end_indx:
        mid_indx = (st_indx + end_indx) // 2
        mid_num = input_list[mid_indx]
        
        if mid_num >= first_num:
            st_indx = mid_indx
        else:
            end_indx = mid_indx
            
        if (st_indx + 1) == end_indx:
            return end_indx
            
    return -1

           
           

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

#edge cases
test_function([[6, 7, 8, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[6, 7], 6])