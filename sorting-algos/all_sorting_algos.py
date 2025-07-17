import random

def bsort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bsort2(arr):
    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(1, n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                is_sorted = False
        n -= 1
    return arr
    
def ins_sort(arr):
    for i in range(1, len(arr)):
        picked = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > picked:
            arr[j+1] = arr[j]
            j -= 1
        # when the loop breaks, j will be off by one towards the left of the insertion breakpoint
        arr[j+1] = picked
    return arr
    
def sel_sort(arr):
    n = len(arr)
    min_index = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
def merge_sort(arr):
    n = len(arr)
    if n == 1: # BASE CASE IMPORTANT
        return arr
    
    mid = n // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    sorted_arr = [0] * n
    l, r = 0, 0
    l_len, r_len = len(left), len(right)
    i = 0
    
    while l < l_len and r < r_len:
        if left[l] < right[r]:
            sorted_arr[i] = left[l]
            l += 1
        else:
            sorted_arr[i] = right[r]
            r += 1
        i += 1
    
    while l < l_len:
        sorted_arr[i] = left[l]
        l += 1
        i += 1

    while r < r_len:
        sorted_arr[i] = right[r]
        r += 1
        i += 1
    
    return sorted_arr
        
def q_sort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[-1]
    left = [x for x in arr[:-1] if x < p]
    right = [x for x in arr[:-1] if x > p]
    
    return q_sort(left) + [p] + q_sort(right)
    
def counting_sort(arr):
    max_el = arr[0]
    for x in arr:
        if x > max_el:
            max_el = x
    
    count_arr = [0] * (max_el + 1)
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    count_ind = 0
    for i in range(len(count_arr)):
        while count_arr[i] > 0:
            arr[count_ind] = i
            count_ind += 1
            count_arr[i] -= 1
            
    return arr

unsorted_arr = random.sample(range(1, 100), k = 6)
print("unsorted arr: ", unsorted_arr)
print(q_sort(unsorted_arr))

unsorted_count_arr = random.choices(range(1, 4), k = 7)
print("unsorted count arr: ", unsorted_count_arr)
print(counting_sort(unsorted_count_arr))