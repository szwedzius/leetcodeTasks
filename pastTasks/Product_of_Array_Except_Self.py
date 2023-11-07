#Its a simple question thats needs for us to count the prefix and sufix products of values
#Example [1,2,3,4]
#Prefix product array [1,2,6,24]
#Sufix product array [24,24,12,4]
#Now look if you want the product of products without 2
#then u take the prefix product to the left and the sufix product to the right and multiply them
# 1 * 12 = 12 correct
# 4 * 2 = 8 correct
# 24 correct
# 6 correct

def productExceptSelf(self, nums: list[int]) -> list[int]:
    #lets create the necessary arrays
    prefix = [nums[0]]
    sufix = [nums[-1]]
    for i in range(1,len(nums)):
        prefix.append(nums[i] * prefix[i-1])
        sufix.append(nums[len(nums)-i-1] * sufix[i-1])
    sufix.reverse()
    result = [sufix[1]]
    for i in range(1,len(nums)-1):
        result.append(prefix[i-1]*sufix[i+1])
    result.append(prefix[-2])
    return result

print(productExceptSelf(0,[1,2,3,4]))