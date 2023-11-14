def containsDuplicate(self, nums) -> bool:
    numsTuple = set()
    for num in nums:
        numsTuple.add(num)
    return len(numsTuple) == len(nums)


print(containsDuplicate(self="", nums=["1", "2", "3","1"]))
