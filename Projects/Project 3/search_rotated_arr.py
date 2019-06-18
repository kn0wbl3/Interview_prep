# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:37:48 2019

@author: Andrew
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
   
    st_indx = 0
    end_indx = len(input_list) - 1
   
    while st_indx < end_indx:
        mid_indx = (st_indx + end_indx) // 2
        mid_num = input_list[mid_indx]
        st_num = input_list[st_indx]
        end_num = input_list[end_indx]
        
        if number == mid_num:
            return mid_indx
        elif st_num > end_num:
            if (st_num <= number < mid_num):
                end_indx = mid_indx
            else:
                st_indx = mid_indx
        else:
            if (st_num <= number < mid_num):
                end_indx = mid_indx
            else:
                st_indx = mid_indx
            
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
