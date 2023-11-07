def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    counts = [[] for i in range(len(nums) + 1)]
    numSet = set(nums)
    for num in numSet:
        numCount = nums.count(num)
        counts[numCount-1].append(num)

    result = []
    for x in range(len(counts)-1,-1, -1):
        for val in counts[x]:
            if k == 0:
                return result
            result.append(val)
            k-=1
    return result

print(topKFrequent(0,[1,1,1,2,2,3], k = 2))