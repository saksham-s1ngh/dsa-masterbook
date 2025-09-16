"""
Try to solve the Product of Array Except Self problem.

Statement
You’re given an integer array, nums. Return a resultant array product so that product[i] is equal to the product of all the elements of nums except nums[i].

Write an algorithm that runs in O(n) time without using the division operation.

Constraints:
-> 2 <= nums.length <= 10^3
-> 30 <= nums[i] <= 30
-> The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

def find_product(nums):
    
    # Brute-force method
    products = []
    left = 1

    for i in range(len(nums)):
        current_prod = 1 # variable to store prod. of elements on right

        for num in nums[i+1:]: # loop to get prod. of all right elems
            current_prod *= num
        
        products.append(current_prod * left) # multiply prod. of elems on left with elems. on right and append to "products array"

        left *= nums[i] # update left variable by multiplying with current elem (will successively store the prod. of elems on left)

    return products

def find_product_opt(nums):

    # Optimised method (Problem asks for O(n) soln.)
    products = []
    
    # Calculate products of elems starting from left
    # This loop successively stores prod. of all elems on left of 
    #   current elem in loop.
    left = 1
    for i in range(len(nums)):
        products.append(left)
        left *= nums[i]
    
    # Now, using the left prods. stored in "products" array,
    #   take a "right" variable to traverse in the reverse direction
    #   and multiply left prods. successively with prods. of all elems on the right. 
    #   Update the right variable each time to store
    #   the running total product.
    right = 1
    for i in range(len(nums)-1, -1, -1):
        products[i] *= right
        right *= nums[i]

    return products

def main():
    inputs = [
        [1, 2, 3, 4],   
        [5, -3, 1, 2],   
        [2, 2, 2, 0],      
        [0, 0, 0, 0],   
        [-1, -2, -4]   
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tList of products: ", find_product_opt(inputs[i]), sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()