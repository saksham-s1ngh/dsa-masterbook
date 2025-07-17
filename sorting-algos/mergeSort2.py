def merge_sort2(arr): # unified merge and divide implementation of merge sort
    """
    Merge sort 2 is just a unified implementation of merge sort with a single method
    to do the same procedure as done by other merge sort implementations.

    Big O = Big Theta = Big Omega : O(nlogn)
    Space Complexity : O(n)

    uses: large datasets, may be worse for smaller datasets since it needs more space
    compared to algorithms like insertion sort.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    le = arr[:mid]
    ri = arr[mid:]
    merge_sort2(le)
    merge_sort2(ri)

    i = j = k = 0
    le_len, ri_len = len(le), len(ri)

    while i < le_len and j < ri_len:
        if le[i] < ri[j]:
            arr[k] = le[i]
            i += 1
        elif le[i] > ri[j]:
            arr[k] = ri[j]
            j += 1
        k += 1

    while i < le_len:
        arr[k] = le[i]
        i += 1
        k += 1

    while j < ri_len:
        arr[k] = ri[j]
        j += 1
        k += 1

    return arr