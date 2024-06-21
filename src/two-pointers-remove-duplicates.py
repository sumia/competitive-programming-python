#  Removing Duplicates in a Sorted Array
# Time: O(N)
# Space: O(1)

# array: fast/slow pointers
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return arr[:slow + 1]

print(remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]))