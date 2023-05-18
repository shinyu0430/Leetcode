def twoSum(nums,target):
    set = {} # save a set of "target - number"
    for i in range(len(nums)):
        if nums[i] in set:
            return [i,set[nums[i]]]
        set[target-nums[i]] = i
print(twoSum([3,2,4],6))

