def bubble_sort(arr):
    """
    BubbleSort is a sorting algo that "bubbles" the greatest element to the last valid position on each pass.

    Big O = Big Omega = Big Theta: O(n^2)
    Space complexity: O(1)

    uses: almost sorted or sorted data, small lists

    """
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i): # - i to not check sorted elements
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr