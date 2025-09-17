def find_first_unique(nums):
    
    # Brute-force first attempt
    #   Since dictionaries are ordered since Python 3.7+
    #   this solution only works for these versions.

    # Store all num in a dictionary but pop the ones that 
    #   occur more than once. Then return the first key
    #   (which is the first non-repeating integer).
    non_rpt = {}
    for num in nums:
        if num in non_rpt:
            non_rpt.pop(num)
        else:
            non_rpt[num] = 1
    return list(non_rpt.keys())[0]

# Driver code
def main():

    inputs = [
        [9, 2, 3, 2, 6, 6],
        [-5, -4, -4, 6, -1],
        [-1, 2, -1, -4, -10],
        [1, 1, 2, 9],
        [-2, 2, -2, 2, 5]
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tInput list: ", inputs[i], sep="")
        print("\n\tfirst unique number: ", find_first_unique(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()