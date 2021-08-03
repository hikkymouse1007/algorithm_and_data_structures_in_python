from typing import List
def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0 
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        # pythonのrangeの第二引数は+1して計算されるので、0-1 = -1でも、indexの終わりは0
        for i in range(end-1, start-1, -1):
             if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        start = start + 1
    print(numbers)
            
if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    cocktail_sort(nums)
    
    
# >>> [i for i in range(3, -1, -1)]
# [3, 2, 1, 0]
# >>> [i for i in range(3, 0, -1)]
# [3, 2, 1]
# >>> 