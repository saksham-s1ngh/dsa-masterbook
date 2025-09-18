"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-rotate-list

Challenge: Rotate List
Try to solve the Rotate List problem.

Statement
You are given an integer list, nums, and a non-negative integer k. Your task is to rotate the list to the right by k steps.

In a right rotation, the last element moves to the front, and all other elements shift one position to the right.

Constraints:
-> 1<= nums.length <= 10^3
-> -10^5 <= nums[i] <= 10^5
-> 1 <= k <= 10^3
"""

def right_rotate(nums, k):

    # rotations = k % len(nums)
    # My first attempt
    for _ in range((k % len(nums)) ):
        last_elem = nums.pop()
        nums.insert(0, last_elem)
    
    return nums

def right_rotate_2(nums, k):

    # basically an even shorter method utilising
    #   list slicing.
    # the k rotations can also be understood as the
    #   number of elements being lifted from the end
    #   and being placed at the beginning in the same
    #   order.

    k = k % len(nums)

    return nums[len(nums) - k:] + nums[:len(nums)-k]


def main():
    inputs = [
        ([10, 20, 30, 40, 50]),  
        ([1, -2, 3, 4, 5]),  
        ([-1, 90, -90, 4, 6]),      
        ([3, 6, 9, -12]),          
        ([-100, -200, -300])         
    ]
    k= [3, 2, 6, 2, 1]
    
    for i in range(len(inputs)):
        print(i + 1, ".\tnums: ", inputs[i], sep="")
        print("\tk: ", k[i], sep="")
        print("\n\tRotated list: ", right_rotate_2(inputs[i], k[i]), sep="")
        print("-" * 70)

if __name__ == "__main__":
    main()