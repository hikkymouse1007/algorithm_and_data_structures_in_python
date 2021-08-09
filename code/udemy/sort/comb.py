from typing import List
def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        print(i)
        for j in range(len_numbers -1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(numbers)
            
if __name__ == '__main__':
    nums = [2, 5, 1, 8, 7, 3]
    comb_sort(nums)