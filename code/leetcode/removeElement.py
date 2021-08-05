from typing import List
def removeElement(nums: List, val: int) -> int:
    remain_nums = [i for i in nums if i != val]
    print(remain_nums)
    return (len(remain_nums), remain_nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))