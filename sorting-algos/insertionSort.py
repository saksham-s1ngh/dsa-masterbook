def insertion_sort(arr):
    """
    Insertion sort algorithm works by first picking an element and then using 
    another loop to compare elements. 
    (For ascending order) Starting from a position previous to the picked 
    element, we move backwards and compare each element with picked element 
    and slide them to right if element > picked_element.
    By the time we reach an index where picked element is greater than the element, 
    we'd have moved all elements greater than picked element and now we just 
    "insert" the element in its correct position.

    Big O = Big Theta: O(n^2)
    Big Omega: O(n)
    Space complexity: O(1)

    """
    for i in range(1, len(arr)):
        picked_element = arr[i] # we pick an element
        j = i - 1 # pick a position previous to picked element's index
        # we move backwards and compare elements with picked element,
        #   moving all elements greater than picked element (for ascending)
        while j >= 0 and picked_element < arr[j]:
            arr[j + 1] = arr[j] # slide elements to the right (ascending) to find the correct spot for picked element
            j -= 1 
        # once the inner while loop concludes, we'd have moved all elements
        #   greater than picked_element, and now we just insert picked
        #   element in the correct position
        arr[j + 1] = picked_element

    return arr
