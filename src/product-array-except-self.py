# You are given an array of integers. 
# Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.
# You cannot use division in this problem.

# Input: [1, 2, 3, 4, 5] 
# Output: [120, 60, 40, 30, 24].


def products(nums):
    # generate prefixes
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # generate suffixes
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # result
    results = []
    for i in range(len(nums)):
        if i == 0:
            results.append(suffix_products[i+1])
        elif i == len(nums) - 1:
            results.append(prefix_products[i-1])
        else:
            results.append(prefix_products[i-1] * suffix_products[i+1])
    
    return results


print(products([1, 2, 3, 4, 5]))

# Time : O(n)
# Space: O(n)