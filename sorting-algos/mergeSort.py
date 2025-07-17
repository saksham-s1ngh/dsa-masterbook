def merge_sort(arr):
    """
    Merge sort is an algorithm utilising the "divide-and-conquer" principle,
    recursively dividing the array into two parts until each array has a single
    element.
    Once we reach single length arrays, we merge arrays by comparing and sorting
    them along the way.

    Big O = Big Theta = Big Omega : O(nlogn)
    Space Complexity : O(n)

    uses: large datasets, may be worse for smaller datasets since it needs more space
    compared to algorithms like insertion sort.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(le, ri):
    i = j = k = 0
    le_len, ri_len = len(le), len(ri)
    res = [0]*(le_len + ri_len)

    while i < le_len and j < ri_len:
        if le[i] < ri[j]:
            res[k] = le[i]
            i += 1
        elif le[i] > ri[j]:
            res[k] = ri[j]
            j += 1
        k += 1

    while i < le_len:
        res[k] = le[i]
        i += 1
        k += 1

    while j < ri_len:
        res[k] = ri[j]
        j += 1
        k += 1

    return res