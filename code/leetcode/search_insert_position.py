from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    nums.append(target)
    sorted_nums = sorted(nums)
    print(sorted_nums)
    index = 0
    for idx, num in enumerate(sorted_nums):
        if num == target:
            index = idx
            break
    return index
    
nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target))
