from typing import List

class Solution:
    def threesum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list_of_triplets = []

        for i in range(len(nums) - 2):
            if(i > 0 and i < len(nums) and nums[i] == nums[i - 1]):
                continue

            left, right = i + 1, len(nums) - 1 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if(total == 0):
                    list_of_triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
            
        return list_of_triplets

    def display(list_of_lists):
        if not list_of_lists:
            return "[]"
        
        result = "["
        for i, lst in enumerate(list_of_lists):
            result += "["
            result += ", ".join(map(str, lst))
            result += "]"

            if i < len(list_of_lists) - 1:
                result += ", "
        
        result += "]"
        return result


solution = Solution()
res = solution.threesum([0,0,0])
print(res) # output: [0,0,0]

res = solution.threesum([-1,0,1,2,-1,-4])
print(res) # output: [[-1,-1,2],[-1,0,1]]

res = solution.threesum([0,1,1])
print(res) # output: []


