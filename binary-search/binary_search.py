
import random
import time
# Implementation fo binary search algorithm!!

# We will prove that binary search is faster than a native search.

# native search: scan entire list and ask if it is equal to the target
#if yes, return the index
# if no, then return -1
def native_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

    # binary search uses divide and conquer! 
    # we will leverage the fact that our list is SORTED in order to make our search FASTER
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    # example l = [1, 3, 5, 10, 12]
    midpoint = (low + high) // 2 # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(native_search(l, target))
    print(binary_search(l, target))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        native_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")
    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")

