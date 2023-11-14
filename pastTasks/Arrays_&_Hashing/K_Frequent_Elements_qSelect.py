def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    numSet = set(nums)
    numDict = {}
    for num in numSet:
        numCount = nums.count(num)
        numDict[num] = numCount

    quickSelectArray = numDict.values()
    print([*quickSelectArray])
    result = quick_select([*quickSelectArray],k, 0, len(quickSelectArray)-1)
    res = []
    for x in range(0,len(result)):
        res.append(numDict[result[x]])

    return res

def quick_select(array, k, left, right):
    partition_temp, partition_index = partition(array,0,len(array)-1)
    if partition_index+1 == k:
        return partition_temp[partition_index:len(partition_temp)]
    elif partition_index+1 > k:
        return quick_select(partition_temp,k,0,partition_index)
    else:
        return quick_select(partition_temp,k,partition_index+1,len(array)-1)



def partition(array, left, right):
    #setup
    pivotIndex = int((right-left)/2)
    temp = array[right]
    array[right] = array[pivotIndex]
    array[pivotIndex] = temp
    swapIndex = left
    #main loop
    for i in range(left,right):
        if array[i] < array[right]:
            if i != swapIndex:
                temp = array[i]
                array[i] = array[swapIndex]
                array[swapIndex] = temp
                swapIndex+=1

    temp = array[right]
    array[right] = array[swapIndex]
    array[swapIndex] = temp

    return array,swapIndex



#partition([5,2,4,3,1],0,4)
topKFrequent(0,[1,2],2)