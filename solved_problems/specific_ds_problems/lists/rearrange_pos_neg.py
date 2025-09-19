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

    # MyFA:
    # Use a single pointer 'left' inside a loop, whenever the looping variable encounters
    #   a negative num, swap with left ptr and increment left?

    left = 0
    for index in range(len(lst)):
        if lst[index] < 0:
            lst[left], lst[index] = lst[index], lst[left]
            left += 1

    return lst

def rearrange_auxL(lst):

    # Brute method : Using 2 auxilliary lists
    #   one list has negatives, other has positives
    #   separate original into these 2, then merge
    # Suppose this method is advantageous for in-place ordering
    neg = []
    pos = []

    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
        
    return neg + pos

def rearrange_pythonic(lst):

    # Pythonic solution: Same as optimal
    #   But this employs list comprehension to filter
    #   positives and negatives and then return them 
    #   as a single combined list.

    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

def main():
    inputs = [[10, 4, 6, 23, 7],
              [-3, 20, -1, 8],
              [2, -5, -4, 43, 2],
              [-3, -10, -19, 21, -17],
              [25, 50, 75, -100, 400]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", rearrange_pythonic(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()