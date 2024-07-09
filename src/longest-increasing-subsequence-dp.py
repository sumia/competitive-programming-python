# input [10, 9, 2, 5, 3, 3, 7, 101, 18]
# output 4 
# Explanation: The longest increasing subsequence is [2, 3, 7, 18], for a total length of 4.

# Time: O(n^2), two nested loops
# Space: O(n), as in worst case all the numbers in the array can be in increasing order

from typing import List

def longest_increasing_subsequence(nums: List[int]) -> int:
    dp = [1] * len(nums)
    output = []

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                if(dp[i] < dp[j] + 1):
                    output.append(dp[j])
                    print(output)


    return dp

print(longest_increasing_subsequence([10, 9, 2, 5, 3, 3, 7, 101, 18]))