# input [10, 9, 2, 5, 3, 3, 7, 101, 18]
# output 4 
# Explanation: The longest increasing subsequence is [2, 3, 7, 18], for a total length of 4.

# Time: O(nlgn), one loop (n) and binary search cuts the result into half each time (lgn)
# Space: O(n), as in worst case all the numbers in the array can be in increasing order

from typing import List
def longest_increasing_subsequence(nums: List[int]):
    tails = []
    count = 0
    for num in nums:
        count += 1
        index = bisect_left(tails, num)
        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num
        print(f"{count} {tails}")
    return tails

def bisect_left(tails: List[int], num: int):
    left = 0
    right = len(tails) 

    while left < right:
        mid = (left + right) // 2
        if num > tails[mid]:
            left = mid + 1
        else:
            right = mid

    return left

res = longest_increasing_subsequence([10, 9, 2, 5, 3, 3, 7, 101, 18])
print(f"Output:: {res}, length: {len(res)}")