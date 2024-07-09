# The Counting Sort algorithm sorts an array by counting the number of times each value occurs.

# Space: 1, 

from typing import List

class Solution:
    def sort_color(self, nums:List[int]) -> None: 
        max_val = max(nums)
        counts = [0] * (max_val + 1)

        for num in nums:
            counts[num] += 1
        
        index = 0
        for i in range(len(counts)):
            while counts[i] > 0:
                nums[index] = i
                counts[i] -= 1
                index += 1

        return nums
    
print(Solution().sort_color([2, 0, 2, 1, 1, 2])) # Output: [0, 1, 1, 2, 2, 2]
print(Solution().sort_color([4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3])) # Output: [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]
        
