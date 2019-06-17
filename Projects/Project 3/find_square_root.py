import math #only used for test cases

def sqrt(number):
    """
    Calculate the floored square root of a number. This implementation walks from 0 to the number, let's call this i, and tries to find the sqrt root by squaring i each time to see if it is close to number.

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number <= 1:
        return number
    
    floor = float('inf')
    
    for i in range(number):
        poss_square = i*i
        if (number - poss_square) == 0:
            return i
        elif ((number - poss_square) < floor) and ((number - poss_square) > 0):
            floor = (number - poss_square)
        else:
            return i-1 #this returns the floor value
        

def sqrt_bs(number):
    st = 0
    end = number
    
    
    while st <= end:
        mid = (st+end) // 2
        poss_square = (mid*mid)
        if poss_square == number:
            return mid
        elif (poss_square  - number) < 0 and (((mid+1) * (mid+1))  - number) > 0: #if the mid^2 is smaller than the number and (mid+1)^2 is larger than the number then we know we need to take the floor value, which is the mid
            return mid
        elif (poss_square  - number) > 0:
            end = mid - 1
        else:
            st = mid + 1
            
        

def tests():
    #LINEAR 
    assert(3 == sqrt(9))
    assert(4 == sqrt(16))
    assert(1 == sqrt(1))
    assert(5 == sqrt(27))
    #edge cases
    assert(sqrt(30024561) == math.floor(math.sqrt(30024561)))
    assert(0 == sqrt(0))
    
    assert(3 == sqrt_bs(9))
    assert(4 == sqrt_bs(16))
    assert(1 == sqrt_bs(1))
    assert(5 == sqrt_bs(27))
    #edge cases
    assert(sqrt_bs(30024561) == math.floor(math.sqrt(30024561)))
    assert(0 == sqrt_bs(0))
    
    print('tests done')
    
tests()