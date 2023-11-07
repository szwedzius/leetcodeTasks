def twoSum(self, nums: list[int], target: int) -> list[int]:
    searched_values = {}
    for i in range(0,len(nums)):
        searched_index = searched_values.get(target - nums[i])
        if searched_values.get(target-nums[i]) is not None:
            return [i, searched_index]
        searched_values[nums[i]] = i

print(twoSum(self="xdd", nums=[2, 7, 11, 15], target=9))
print(twoSum(self="xdd", nums=[3, 2, 4], target=6))
print(twoSum(self="xdd", nums=[3, 3], target=6))
