from typing import List
def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    print(range(len_numbers))
    for i in range(len_numbers):
        min_idx = i
        for j in range(i+1, len_numbers):
            print(numbers[min_idx])
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        
    return numbers
    
if __name__ == '__main__':
    numbers = [2, 5, 1, 8, 7, 3]
    print(selection_sort(numbers))