def quick_sort(arr, first_i, last_i):
    """
    Quicksort algorithm is an algorithm relying on the "divide-and-conquer" principle
    by breaking the problem into smaller components and sorting these smaller components.
    It does this in-place as compared to merge-sort.

    Big O : O(n^2)
    Big Theta = Big Omega : O(nlogn)
    Space complexity: O(logn) -> can be O(n) in worst case

    uses: large datasets in memory-constrained environments
    """
    if first_i < last_i:
        partition_i = partition(arr, first_i, last_i)
        quick_sort(arr, first_i, partition_i)
        quick_sort(arr, (partition_i + 1), last_i)
    
    return arr


def partition(arr, first_i, last_i):
    pivot = arr[first_i]
    left_p = first_i + 1
    right_p = last_i

    while True:
        # we traverse until we left_pointer points to a value greater than pivot
        #   and till left_pointer is less than last index
        while arr[left_p] < pivot and left_p < last_i:
            left_p += 1
        while arr[right_p] > pivot and right_p >= first_i:
            right_p -= 1
        # the loop should break if the pointers cross each other
        #   this happens when, when all elements towards left (elements that
        #   left_pointer has crossed) are <= pivot
        #   and the elements towards right (elements 
        #   that right_pointer has) are > pivot
        if left_p >= right_p:
            break
        # if we didn't break out, we'd have found positions of 2 elements :
        #   on the left, an element greater than pivot and 
        #   on the right, an element smaller than pivot
        #   as such we swap the two.
        arr[left_p], arr[right_p] = arr[right_p], arr[left_p]
    # if the loop breaks (pointers crossed), we swap the pivot with right_pointer
    #   since the right_pointer is at the position that the pivot is supposed to 
    #   be and thus we swap the two. (right_p points to greatest element <= pivot)
    arr[first_i], arr[right_p] = arr[right_p], arr[first_i]

    return right_p