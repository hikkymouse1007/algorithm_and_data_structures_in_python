from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        print("target:", target, "num:", num)
        search_key = target - num
        print("search_key:", search_key, "target:", target, "num:", num)
        if search_key not in hashmap:
            hashmap[num] = i
            print("hashmap:", hashmap) # num2であれば、1は0番目、7は1番目に入っている
        else:
            print(i, hashmap[search_key])
            return [i, hashmap[search_key]]

nums = [2,7,11,15]
nums2 = [1,7,2,15]
target = 9

# print(twoSum(nums, target))
print(twoSum(nums2, target))
