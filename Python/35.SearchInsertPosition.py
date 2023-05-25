# Solution1: Time:O(n)/Space:O(n)
def searchInsert(self, nums: List[int], target: int) -> int:
    i = 0

    while i < len(nums) and nums[i] < target:
        i += 1
    return i

# Solution2: Time:O(logn)
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] == target:
            return mid
        else:
            right = mid-1
    return left
