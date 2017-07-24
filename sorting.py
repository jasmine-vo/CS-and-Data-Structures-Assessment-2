#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    # Sets each index to swapped = False.  This helps us keep track of what
    # has been swapped. 
    for index in range(len(lst) - 1):
        swapped = False

        # Checks each number at index to see if the next number is greater. If 
        # so, both numbers are swapped.
        for num in range(len(lst) - 1 - index):
            if lst[num] > lst[num + 1]:
                lst[num], lst[num + 1] = lst[num + 1], lst[num]
                swapped = True
        if not swapped:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged_sorted_list = []

    # Loops until one of the lists is empty
    while list1 != [] or list2 != []:

        # If one of the lists is empty, pops the first element in the other list
        # and appends to the merged_sorted_list.
        if list1 == []:
            merged_sorted_list.append(list2.pop(0))

        elif list2 == []:
            merged_sorted_list.append(list1.pop(0))

        # Checks if the first item in list1 is smaller than list2, if it is, it
        # pops the first item from list1 and appends to the merged_sorted_list.
        elif list1[0] < list2[0]:
            merged_sorted_list.append(list1.pop(0))

        else:
            merged_sorted_list.append(list2.pop(0))

    return merged_sorted_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    # Checks if length of list is less than two.  If the length of the list is
    # one, it is already sorted.  If it is empty, there is nothing to sort.
    if len(lst) < 2:
        return lst

    # Get the index in the middle of the list
    mid = len(lst) / 2

    # Uses slicing and the mid variable to split the list in halves.
    list1 = merge_sort(lst[:mid])
    list2 = merge_sort(lst[mid:])

    # Uses the earlier function, merge_lists, to merge the two lists
    return merge_lists(list1, list2)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
