#Sorting 
def quicksort(num_list):
    """
    Recursive O(n log(n)) sorting algorithm
    """
    if num_list == []:
        return num_list
    else:
        pivot = num_list[0]
        lesser = [num for num in num_list if num < pivot]
        pivots = [num for num in num_list if num == pivot]
        greater = [num for num in num_list if num > pivot]
        return quicksort(lesser) + pivots + quicksort(greater)
    
def binary_search(ordered_list, lower, upper, item):
    if lower + 1 == upper:
        return item == ordered_list[lower]    
    mid = (lower + upper) / 2
    if item < ordered_list[mid]:
        return binary_search(ordered_list, lower, mid, item)
    else:
        return binary_search(ordered_list, mid, upper, item)



