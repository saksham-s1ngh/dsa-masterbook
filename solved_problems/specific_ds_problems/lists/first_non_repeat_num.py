def find_first_unique(nums):
    
    # Brute-force first attempt
    #   Since dictionaries are ordered since Python 3.7+
    #   this solution only works for these versions.

    # Store all num in a dictionary but pop the ones that 
    #   occur more than once. Then return the first key
    #   (which is the first non-repeating integer).
    non_rpt = {}
    for num in nums:
        if num in non_rpt: # this step adds O(n) complexity
            non_rpt.pop(num)
        else:
            non_rpt[num] = 1
    return list(non_rpt.keys())[0]

def find_first_unique_brute(nums):
    
    # Brute attempt with 2 pointers

    # Traverse through the list with 1 pointer
    for p1 in range(len(nums)):
        p2 = 0

        # use the 2nd pointer to compare with 1st
        #   if they're equal, increment 1st pointer
        #   else increment 2nd pointer
        while p2 < len(nums):
            if nums[p1] == nums[p2] and p1 != p2:
                break
            p2 += 1

        # if the 2nd pointer traverses entire list without break
        #   then the first pointer is pointing to the unique element.
        if p2 == len(nums):
            return nums[p1]
    
    return None
    
def find_first_unique_opt(nums):
    
    # optimised method: store frequencies then return the first num
    #   with 1 occurrence.

    # First pass to store frequencies
    freq = {}
    for num in nums:
        # the dict.get(key, 0) statement tries to fetch a value
        #   for the given key, and if not found sets it to the
        #   given value which is 0 here.
        freq[num] = freq.get(num, 0) + 1
    
    for num in nums:
        if freq[num] == 1:
            return num

    return None

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
        print("\n\tfirst unique number: ", find_first_unique_opt(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()