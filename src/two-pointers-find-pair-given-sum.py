# Given a sorted array, find two numbers that add up to a target sum.
# Time: O(N)
# Space: O(1)

# array: left/right pointers
def find_pair_with_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right] 
        if sum == target:
            return (left + 1, right + 1)
        if sum < target:
            left += 1
        else: 
            right -= 1

    return None
        
print(find_pair_with_sum([1, 2, 3, 4, 6], 6))