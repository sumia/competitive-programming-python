#The Dutch National Flag algorithm was proposed by Edsger W. Dijkstra. It provides an efficient way to sort an array of three distinct elements, often #referred to as sorting the colors in an array. The algorithm divides the array into three sections and sorts it in a single pass.

# Time: O(n), one loop
# Space: 1, 

from typing import List

class Solution:
    def sort_color(self, nums:List[int]) -> None: 
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        return nums
    
print(Solution().sort_color([2, 0, 2, 1, 1, 2]))
        
