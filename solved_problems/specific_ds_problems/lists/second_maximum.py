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

def main():
    inputs = [[9, 2, 3, 6],
            [1, 2],
            [-2, 2],
            [-4, -1, -9, 1, -7],
            [25, 50, 75, 100, 100]]

    for i in range(len(inputs)):
        print(i + 1, ".\tList: ", inputs[i], sep="")
        print("\n\tSecond maximum value: ", find_second_maximum(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()