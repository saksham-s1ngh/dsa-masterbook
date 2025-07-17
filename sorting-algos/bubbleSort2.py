def bubble_sort2(arr):
    """
    BubbleSort2 is an improved version of the original BubbleSort.
    A flag is used to check if the list is already sorted, and if so return out immediately.

    Big O = Big Theta : O(n^2)
    Big Omega : O(n)
    Space Complexity : O(1)

    """
    arr_len = len(arr)
    is_sorted = False

    while not is_sorted: # while not False => while True
        is_sorted = True
        # the reason for setting "list_length-1" as the range end is
        #   because we're comparing the (i) value with (i+1) value
        #   so it avoids IndexErrors

        # another alternative maybe, to set range (1, arr_len)
        #   and compare (i-1) and (i)
        for i in range(arr_len - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # we're setting the flag to False again, because we've 
                #   discovered the list is unsorted and want to make sure 
                #   it's sorted before returning.
                
                # if the flag stays true, the program exits the while loop
                #   and the list is returned (for case: sorted list)
                is_sorted = False
        arr_len -= 1 # reduce the list length to not check sorted values again

    return arr
