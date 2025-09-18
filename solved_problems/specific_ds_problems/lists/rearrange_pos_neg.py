"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-rearrange-positive-negative-values

Rearrange Positive & Negative Values
Try to solve the Rearrange Positive & Negative Values problem.

Statement
Implement a function that rearranges elements in a list so that all negative elements appear to the left and all positive elements (including zero) appear to the right. It’s important to note that maintaining the original sorted order of the input list is not required for this task.

Constraints:
• 1 ≤ lst.length ≤ 10^3 
• 10^-5 ≤ lst[i] ≤ 10^5
"""

def rearrange(lst):

    # [1, -2, 3, -5, 4, -8, 6]
    # MyFA. Sorting would be O(nlogn)
    # Use a single pointer 'left' inside a loop, whenever the looping variable encounters
    #   a negative num, swap with left ptr and increment left?

    left = 0
    for index in range(len(lst)):
        if lst[index] < 0:
            lst[left], lst[index] = lst[index], lst[left]
            left += 1

    return lst

def main():
    inputs = [[10, 4, 6, 23, 7],
              [-3, 20, -1, 8],
              [2, -5, -4, 43, 2],
              [-3, -10, -19, 21, -17],
              [25, 50, 75, -100, 400]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", rearrange(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()