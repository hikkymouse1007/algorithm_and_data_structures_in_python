from typing import List, NewType

IndexNum = NewType('IndexNum', int)

def liner_search(numbers: List[int], value: int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            print(i)
            return i
    return -1 #見つからなかったら-1を返す
    
# def binary_search(numbers: List[int], value: int) -> IndexNum:
#     left, right = 0, len(numbers) - 1
#     while left <= right:
#         print("#####")
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value: # midより右にvalueがあるとき
#             left = mid + 1
#         else:                      # midより左にvalueがあるとき
#             right = mid - 1
#     return -1                      #見つからなければ -1


# recursive
def binary_search(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], value: int,
                        left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else: 
            return _binary_search(numbers, value, left, mid - 1)
    return _binary_search(numbers, value, 0, len(numbers))
            
         
if __name__ == '__main__': 
    # numbers = [2, 5, 1, 8, 7, 3]
    # print(liner_search(numbers, 7))
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(binary_search(nums, 24))