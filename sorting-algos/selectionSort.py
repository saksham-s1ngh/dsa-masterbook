def selection_sort(arr):
    """
    Selection sort is an algorithm that works by "selecting" the smallest element 
    (for ascending order) and swapping it with the lowest valid position.

    Big O = Big Theta = Big Omega: O(n^2)
    Space complexity : O(1)
    """
    arr_len = len(arr)
    # we only traverse till array_length - 1 since by the time we reach last node
    #   list would already be sorted
    for i in range(arr_len - 1):
        lowest = arr[i]
        index = i
        # inner loops runs to "select" lowest element
        for j in range(i + 1, arr_len):
            if arr[j] < lowest:
                lowest = arr[j]
                index = j
        # swap selected element with the lowest valid index (i)
        arr[i], arr[index] = arr[index], arr[i]

    return arr