def find_second_maximum(nums):
    if nums[0] > nums[1]:
        max = nums[0]
        second_max = nums[1]
    else:
        max = nums[1]
        second_max = nums[0]

    for num in nums[2:]:
        if num > max:
            second_max = max
            max = num
        if max > num > second_max:
            second_max = num

    return second_max

def find_second_maximum_opt(nums):

    first_max = second_max = float("-inf")

    for num in nums:
        if num > first_max:
            second_max = first_max
            first_max = num
        
        elif first_max > num > second_max:
            second_max = num

    return second_max

def main():
    inputs = [[9, 2, 3, 6],
            [1, 2],
            [-2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 100]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tSecond maximum value: ", find_second_maximum_opt(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()