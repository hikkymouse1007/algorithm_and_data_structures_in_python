from typing import List
def removeDuplicates(nums: List) -> List:
    print(nums[:])
    print(set(nums))
    nums[:] = sorted(set(nums))
    return len(nums)

nums = [1,1,2]
print(removeDuplicates(nums))