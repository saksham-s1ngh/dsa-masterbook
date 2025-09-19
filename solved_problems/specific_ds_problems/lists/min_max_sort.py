"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-rearrange-sorted-list-in-max-min-form

Rearrange Sorted List in Max/Min Form
Try to solve the Rearrange Sorted List in Max/Min Form problem.

Statement
We're given a sorted list, nums, containing positive integers only. We have to rearrange the list so that when returned, the 0th index of the list will have the largest number, the 1st index will have the smallest number, the  2nd index will have the second largest number, the 3rd index will have the second smallest number, and so on.

In the end, we’ll have the largest remaining numbers in descending order and the smallest in ascending order at even and odd positions, respectively.

Constraints:
• 0 ≤ nums.length ≤ 10^3
• 0 ≤ nums[i] ≤ 10^5

"""
def rearrange_list(nums):

    # thought process: used a ptr to store index of insertion point
    #   traverse iteratively using a 2 step(move 2 steps instead of 1) 
    #   and pop the max element and then insert it in the correct position.  
    # MyFA :     

    left = 0

    for _ in range(0, len(nums), 2):
        elem = nums.pop()
        nums.insert(left, elem)
        left += 2

    return nums

def rearrange_list_brute(nums):

    # using an auxiliary list, iterate through list
    #   and append max and mins in sequence each iteration
    # max is nums[-(i+1)] and min is nums[i] on each iteration.

    result = []
    mid = len(nums)//2

    for i in range(mid):
        result.append(nums[-(i+1)])

        result.append(nums[i])

    if mid % 2:
        result.append(nums[mid])
    
    return result


def main():
    input_list = [[1, 2, 3, 4, 5, 6, 7, 8],
				  [11, 22, 33, 44, 55, 66, 77, 88],
				  [1, 2, 4, 8, 16, 32, 64, 128, 512, 1024],
				  [3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13],
				  [100, 233, 544, 753, 864, 935, 1933, 2342]]

    for i in range(len(input_list)):
        print(i + 1, ".\tOriginal list: ", input_list[i], sep='')
        print("\tRearranged list: ", rearrange_list_brute(input_list[i]), sep='')
        print("-" * 100)


if __name__ == '__main__':
    main()