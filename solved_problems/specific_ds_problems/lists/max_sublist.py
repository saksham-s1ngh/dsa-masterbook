"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-maximum-sublist

Maximum Sublist
Try to solve the Maximum Sublist problem.

Statement
Given an unsorted list nums, find the sum of the maximum sum sublist. The maximum sum sublist is a list of contiguous elements in nums for which the sum of the elements is maximum.

Constraints:
• 1 ≤ nums.length ≤ 10^3
• -10^4 ≤ nums[i] ≤ 10^4

"""
    # MyFA: was unable to find a working soln.
    # thought process: was hoping to keep an external variable to store max sublist sum, and use a seperate variable within 
    #   the loop to keep a running sum, but couldn't figure out the method to track and store the highest sum upon occurring
    #   a second contiguous sublist.

    # Solution: this problem utilises dynamic programming using Kadane's algorithm which uses a bottoms-up approach to solve
    #   problems iteratively.
    # It does so using 2 variables, curr_max to store current max within the loop and global_max to store the maximum sublist
    #   sum within the list.
def find_max_sum_sublist(nums):
    if len(nums) < 1:
        return 0
        
    curr_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        if curr_max < 0:
            curr_max = nums[i]
        else:
            curr_max += nums[i]
        if global_max < curr_max:
            global_max += nums[i]
    
    return global_max


def main():
    inputs = [[1, 2, 2, 3, 3, 1, 4], [2, 2, 1], [4, 1, 2, 1, 2], [-4, -1, -2, -1, -2],[-4, 2, -5, 1, 2, 3, 6, -5, 1], [25]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\tMaximum Sum: ", find_max_sum_sublist(inputs[i]), sep="")
        print("-" * 75)


if __name__ == "__main__":
    main()