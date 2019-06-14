"""
Bubble sort is a simple sorting algo that sorts data in worst case O(n^2). It compares two pieces of data in a list and swaps them if they are out of order.
"""

def bubble_sort(l):
    if len(l) == 0:
        return None
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index], l[index - 1] = l[index - 1], l[index]

#test1          
wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
bubble_sort(wakeup_times)
print ("Pass" if (wakeup_times[0] == 3) else "Fail")

#test12    
wakeup_times = []
ans = bubble_sort(wakeup_times)
assert(ans == None)
